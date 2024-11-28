
diffusion因为是马尔科夫链,所以并不是适合去做去噪处理的方法,这里添加了clip做
 
 Inversion-Based Style Transfer with Diffusion Models


文章是通过一张style image,通过clip把图片信息进行编码,然后提取成一些风格特征信息,再经过diffusion中的u-net来去把提取的clip信息进行传递加噪和去噪,最后就生成照片信息了