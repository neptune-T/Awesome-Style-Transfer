However, the approach of (Gatys et al., 2015a;b) has certain shortcomings too. Being based on an iterative optimization procedure, it requires backpropagation to gradually change the values of the pixels until the desired statistics is matched. This iterative procedure requires several seconds in order to generate a relatively small image using a high-end GPU, while scaling to large images is problematic because of high memory requirements. By contrast, feed-forward generation networks can be expected to be much more efficient because they require a single evaluation of the network and do not incur in the cost of backpropagation.



$$
\arg\min_{x \in \mathcal{X}} \|\Phi(x) - \Phi(x_0)\|_2^2
$$
- $\Phi(x)$：表示图像 x  在神经网络某个层次上的特征表示（通常是卷积层输出）。
- $\Phi(x_0)$**：表示参考图像 $x_0$ 的特征表示（如风格图像的特征）。
- **目标**：通过最小化生成图像的特征表示与参考图像特征表示之间的差异，使生成图像 x  的风格或纹理接近参考图像 $x_0$。



$$
\text{localopt} \left( \|\Phi(x) - \Phi(x_0)\|_2^2 ; \mathcal{A}, z \right), \quad z \sim \mathcal{N}(0, \Sigma)
$$
- $z \sim \mathcal{N}(0, \Sigma)$：表示从均值为0、协方差为 $\Sigma$ 的正态分布中采样随机噪声  z ，作为图像生成的初始输入。
- $\mathcal{A}$：表示局部优化算法，用于从初始噪声  z  开始，逐步调整生成的图像 x ，使其特征表示与目标图像 $\Phi(x_0)$ 的特征表示匹配。
- $localopt$：代表使用局部优化算法 $\mathcal{A}$ 来最小化特征表示之间的差异。

$$
\phi(x_0) = \frac{1}{|\Omega|} \sum_{i=1}^{|\Omega|} \psi \circ F(x_0; i) \approx E_{x \sim p(x)} \left[ \psi \circ F(x; 0) \right]
$$

对于每一个像素 i，我们先应用滤波器 F 来提取局部特征，然后使用  $\psi$  算子计算这些特征的统计分布，最终对整个图像的每个像素的特征结果进行平均，以获得一个全局的统计量  $\phi(x_0)$。

$$E_{x \sim p(x)} \left[ \psi \circ F(x; 0) \right]$$

表示通过多个随机生成的图像样本，对它们的局部特征进行同样的统计计算，然后取平均值。

最小化左边和右边的差异，我们就可以生成具有相似纹理特征的图像。

![[Pasted image 20241021201539.png]]