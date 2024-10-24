
![[Pasted image 20241024193220.png]]

$$
L_{\text{VAE}} = -\mathbb{E}_{q(z|x)} \left[ \log \frac{p(x|z)p(z)}{q(z|x)} \right] = L_{\text{pixel like}} + L_{\text{prior}}

$$

$$
L_{\text{pixel like}} = - \mathbb{E}_{q(z|x)} \left[ \log p(x|z) \right]
$$

$$
L_{\text{prior}} = D_{\text{KL}} \left( q(z|x) \| p(z) \right)
$$

