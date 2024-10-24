### BN : batch Normalization

$$
\text{IN}(x) = \gamma \left( \frac {x-\mu(x)}{\sigma(x)} \right) + \beta
$$

$$
\mu_c(x) = \frac{1}{NH} \sum_{h=1}^{H} \sum_{w=1}^{W} x_{nchw}
$$

$$
\sigma_c(x) = \sqrt{ \frac{1}{NHW} \sum_{n=1}^{N} \sum_{h=1}^{H} \sum_{w=1}^{W} \left( x_{nchw} - \mu_c(x) \right)^2 + \epsilon }
$$

### AdaIN
$$
\text{AdaIN}(x,y) = \sigma(y) \left(\frac{x-\mu(x)} {\sigma(x)} \right) +\mu(y)
$$

$x$是内容图像的卷积特征表示

$y$是风格图像的卷积特征表示


![[Pasted image 20241022125238.png]]

实际图片和生成图片一同放入,在vgg做特征提取,高层特征是全局结构,底层特征是颜色纹理差异性,现在使用 `AdaIN` 做处理将颜色纹理附到全局结构之中,在使用decoder还原,然后再使用vgg encoder提取与原来的图像信息和纹理细节对比
   $$
   L_s = \sum_{i=1}^{L} \left\| \mu(\phi_i(g(t))) - \mu(\phi_i(s)) \right\|_2 + \sum_{i=1}^{L} \left\| \sigma(\phi_i(g(t))) - \sigma(\phi_i(s)) \right\|_2
  $$
   -  g(t)：表示生成的图像。
   -   s ：表示风格图像。
   -  $\mu(\cdot)$  和 $\sigma(\cdot)$：分别表示在特征图上的均值和标准差，用来衡量图像风格的统计特性。
   