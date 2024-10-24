
### 针对多领域图像转换模型提出的2个问题:

- 当处理多个领域时，需要训练多个生成器，每个生成器只能在两个特定领域之间进行转换，这导致了模型的低效和性能瓶颈。

	比如说有4个不同的领域:A,B,C,D就需要2,2做转换需要12个生成器

- 一个生成器可能只在领域A和领域B之间进行图像的转换学习。这种方式限制了每个生成器的能力，因为它只能学习到两个领域之间的数据，而无法充分利用来自其他领域的数据。


![[Pasted image 20241023153443.png]]

   真实图片
$$
   L_{cls}^r = \mathbb{E}_{x, c'} [- \log D_{cls}(c' | x)]
   $$
   
   生成图像
   $$
   L_{cls}^f = \mathbb{E}_{x, c} [- \log D_{cls}(c | G(x, c))]
  $$

- c 是目标领域的标签 , G(x,c)表示的是图像 x 变换成目标风格的结果


$$
 L_{rec} = \mathbb{E}_{x,c,c'} [\| x - G(G(x, c), c') \|_1] 
$$

   判别器的损失函数
   $$
   L_D = -L_{\text{adv}} + \lambda_{\text{cls}} L_{\text{cls}}^r
   $$
   生成器的损失函数
  $$
  \mathcal{L}_G = \mathcal{L}_{adv} + \lambda_{cls} \mathcal{L}^{f}_{cls} + \lambda_{rec} \mathcal{L}_{rec}
  $$
$$
     \mathcal{L}_{adv} = \mathbb{E}_x[D_{src}(x)] - \mathbb{E}_{x,c}[D_{src}(G(x, c))] - \lambda_{gp} \mathbb{E}_{\hat{x}}[(\|\nabla_{\hat{x}}D_{src}(\hat{x})\|_2 - 1)^2]
$$

  
 

