[[ANeural Algorithm of Artistic Style.pdf]]

![[Pasted image 20241021152152.png]]
内容图像和风格图像首先经过预训练的卷积神经网络（如VGG）提取特征。

内容图像的特征主要捕捉其结构和布局信息，而风格图像的特征则通过Gram矩阵捕捉其全局的颜色和纹理特征。

在这个过程中，生成图像从随机初始化开始，通过不断优化其特征图，使其与内容图像保持结构一致，同时通过最小化生成图像与风格图像的Gram矩阵差异来迁移风格。
  $$
  L_{\text{content}}(I_{\text{gen}}, I_{\text{content}}) = \sum_l \left\| F^l(I_{\text{gen}}) - F^l(I_{\text{content}}) \right\|^2
  $$

  $$
  L_{\text{style}}(I_{\text{gen}}, I_{\text{style}}) = \sum_l \left\| G^l(I_{\text{gen}}) - G^l(I_{\text{style}}) \right\|^2
  $$
  

$$
L_{\text{total}} = \alpha L_{\text{content}} + \beta L_{\text{style}}
$$

在最终损失函数中，内容损失和风格损失按权重相加，通过迭代优化将生成图像调整到既保留内容又体现风格的状态。






