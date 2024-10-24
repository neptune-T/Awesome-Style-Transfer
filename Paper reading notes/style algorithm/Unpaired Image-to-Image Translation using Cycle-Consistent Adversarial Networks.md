
![[Pasted image 20241022212807.png]]

### Adversarial Loss

- 判别器 $D_Y$：区分真实域 $Y$ 图像和由生成器 $G$  生成的假域 $Y$ 图像。
- 判别器 $D_X$：区分真实域 $X$ 图像和由生成器  $F$ 生成的假域 $X$ 图像。

对于生成器 $G$ 和判别器 $D_Y$ 之间的对抗损失为：

$$
\mathcal{L}_{GAN}(G, D_Y, X, Y) = \mathbb{E}_{y \sim p_{data}(y)} [\log D_Y(y)] + \mathbb{E}_{x \sim p_{data}(x)} [\log (1 - D_Y(G(x)))]
$$

对于生成器 $F$ 和判别器 $D_X$ 之间的对抗损失为：

$$
\mathcal{L}_{GAN}(F, D_X, Y, X) = \mathbb{E}_{x \sim p_{data}(x)} [\log D_X(x)] + \mathbb{E}_{y \sim p_{data}(y)} [\log (1 - D_X(F(y)))]
$$

### Cycle Consistency Loss


$$
\mathcal{L}_{cyc}(G, F) = \mathbb{E}_{x \sim p_{data}(x)} [\| F(G(x)) - x \|_1] + \mathbb{E}_{y \sim p_{data}(y)} [\| G(F(y)) - y \|_1]
$$


$$
\mathcal{L}(G, F, D_X, D_Y) = \mathcal{L}_{GAN}(G, D_Y, X, Y) + \mathcal{L}_{GAN}(F, D_X, Y, X) + \lambda \mathcal{L}_{cyc}(G, F)
$$

