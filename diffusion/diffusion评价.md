
diffusion因为是马尔科夫链,所以并不是适合去做去噪处理的方法,这里使用了各种方法来去做风格偏移处理
 
 Inversion-Based Style Transfer with Diffusion Models
 文章是通过一张style image,通过clip把图片信息进行编码,然后提取成一些风格特征信息,再经过diffusion中的u-net来去把提取的clip信息进行传递加噪和去噪,最后就生成照片信息了,但是这一篇的clip本质的核心在于需要自己添加prompt来去作微调,不符合我们说的传统的风格迁移,而且因为需要自己写prompt并且没有限制,能难做到目标图片一致只改变风格

Zero-Shot Contrastive Loss for Text-Guided Diffusion Image Style Transfer
使用difffusion加噪,在去噪中使用clip引导出新的特征信息,而zecon做一致性检测然后得出结论,这里使用了clip加cgan的idea去做一致性处理,这里做了损失优化,用到了多区域检测,保证了每一个地方的一致性,避免出现风格偏移失败的问题

ArtBank: Artistic Style Transfer with Pre-trained Diffusion Model and Implicit Style Prompt Bank
使用了clip做信息检索,创新的使用attention结合提出了代替adain的ssam和存储的ssam,在使用风格处理的时候使用正确的switch做特征处理,经过训练的模型在inference使用随机反转来保证图片的正确性

Style Injection in Diffusion: A Training-free Approach  for Adapting Large-scale Diffusion Models for Style Transfer

