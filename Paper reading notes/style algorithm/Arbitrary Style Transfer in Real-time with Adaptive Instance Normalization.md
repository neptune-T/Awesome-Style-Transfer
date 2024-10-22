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

![[Pasted image 20241022125238.png]]

实际图片和生成图片一同放入,在vgg做特征提取,