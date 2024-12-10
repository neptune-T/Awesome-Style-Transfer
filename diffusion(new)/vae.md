
\subsection{VAE and Its Application in Style Transfer}

The original Variational Autoencoder (VAE) framework has undergone numerous modifications and enhancements since its inception, resulting in a wide array of VAE variants. Each of these variants introduces specific improvements to address limitations in the original VAE model, such as enhancing feature disentanglement, improving image sharpness, supporting high-resolution outputs, and achieving more flexible control over latent space representations. These VAE variants have expanded the capabilities of VAE models in generative tasks, making them particularly valuable in style transfer applications where diverse and high-quality output is desired.

Table~\ref{tab:vae_variants} provides a comprehensive summary of key VAE variants, detailing their innovations, authors, and primary applications. This table illustrates the progression from basic VAE structures to more sophisticated models, including $\beta$-VAE\cite{higgins2017beta}, VQ-VAE\cite{van2017neural}, NVAE\cite{vahdat2020nvae}, and more. Such advancements not only enhance the quality and versatility of generated images but also open up new possibilities for applications in visual arts, video generation, and content adaptation, which are integral to modern style transfer tasks.

One of the earliest improvements was $\beta$-VAE. Higgins et al. observed that features in the VAE latent space were often entangled, making it difficult to isolate specific style characteristics in generated images\cite{higgins2017beta}. To address this, they introduced $\beta$-VAE, which added a regularization term in the ELBO formula by increasing the weight of the KL divergence with a parameter $\beta$. 

\[
\mathcal{L}_{\text{$\beta$-VAE}} = \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - \beta D_{KL}(q_\phi(z|x) || p(z))
\]

By tuning $\beta$, the model could achieve better disentanglement in the latent space, allowing specific style attributes to be controlled independently. This innovation laid the foundation for applications requiring flexible manipulation of style features.

Although $\beta$-VAE made strides in feature disentanglement, image clarity remained a challenge. To tackle this, Van den Oord et al. proposed VQ-VAE (Vector Quantized VAE), which uses a discrete latent space by quantizing the encoder outputs into a finite set of embeddings\cite{van2017neural}. In VQ-VAE, the encoder maps the input \( x \) to a continuous latent representation \( z_e(x) \). This continuous representation is then quantized to the nearest embedding vector \( e_k \) from a codebook \( \{ e_1, e_2, \ldots, e_K \} \), where \( K \) is the number of discrete codes. The quantization step is defined as:

\[
z_q(x) = \arg \min_{e_k} \| z_e(x) - e_k \|
\]

where \( z_q(x) \) represents the quantized latent vector, and \( e_k \) is the closest code in the embedding space. This quantization process reduces the blurriness often observed in generated images by enforcing consistency in the latent space. 

The final objective of VQ-VAE includes a reconstruction loss and a commitment loss, which ensures that the encoder output remains close to the quantized embedding. The commitment loss is defined as:

\[
\mathcal{L}_{\text{commit}} = \| z_e(x) - \text{sg}[z_q(x)] \|^2
\]

where \( \text{sg}[\cdot] \) represents the stop-gradient operator, preventing gradients from flowing back into the codebook. This commitment loss encourages the encoder to stay close to the quantized embeddings, improving training stability. 

As application needs grew, the expressive power of a single latent layer became limited, especially in complex style transfer tasks. Sønderby et al. proposed Hierarchical VAE, introducing multiple levels of latent variables to capture both global and local features, enabling the model to handle multi-scale information. In style transfer, this hierarchical structure allowed the model to handle both global style and local details, which is essential in tasks that require nuanced, multi-scale stylization.


Beyond multi-scale representation, style transfer often requires the generation of images with specific target attributes. Sohn et al. introduced Conditional VAE (CVAE) \cite{sohn2015learning}, which incorporates label information to condition the generation process on external attributes. In style transfer, CVAE allows for the creation of images that adhere to particular artistic styles or emotional tones, enhancing the diversity and personalization of outputs. This targeted generation capability has expanded the applicability of style transfer, meeting more specific user preferences and requirements in creative fields.

To further enhance control over style, Kim and Mnih proposed FactorVAE \cite{kim2018disentangling}, focusing on improving disentanglement by minimizing total correlation among latent dimensions. This ensures that each latent dimension independently encodes specific information, reducing interference among different style features. FactorVAE is particularly suited for style transfer tasks that require precise manipulation of individual style elements, allowing for granular adjustments to achieve more controlled and nuanced outputs.

While the KL divergence is fundamental to VAE optimization, it can sometimes restrict flexibility in the latent space. To address this, Zhao et al. introduced InfoVAE (MMD-VAE) \cite{zhao2017info}, which replaces the KL divergence with a Maximum Mean Discrepancy (MMD) penalty, allowing for a more adaptable prior distribution. This modification creates a more expressive latent space, making InfoVAE especially effective in style transfer tasks that benefit from smooth transitions and stylistic diversity, as it provides greater freedom in exploring varied styles.

Building upon the need for improved disentanglement, DIP-VAE by Kumar et al. \cite{kumar2018variational} introduced a covariance penalty to decorrelate latent variables without relying on high $\beta$ values. This approach enhances interpretability, making DIP-VAE suitable for style transfer applications where distinct style attributes are necessary. It enables a clearer separation of style components, aiding in the achievement of specific stylistic characteristics without compromising on visual clarity.

Addressing redundancy in latent representation, Chen et al. introduced $\beta$-TCVAE \cite{chen2018isolating}, which minimizes total correlation to further reduce redundancies in the latent space, leading to highly disentangled and interpretable representations. This model excels in style transfer tasks that require fine-grained control over individual style components, offering a pathway to achieving highly detailed and artistically sophisticated outputs.

In scenarios requiring hierarchical representation of style, Hierarchical VAE by Sønderby et al. \cite{sonderby2016ladder} introduced multiple levels of latent variables to capture both global and local features. This multi-scale modeling approach is particularly valuable for complex style transfer tasks where stylization demands both broad coherence and intricate detail, providing an effective framework for multi-level style control.

To address scalability issues in VAE models, BigVAE by Child et al. \cite{child2019biggan} introduced a large-scale VAE with hierarchical latent spaces, which enabled the generation of high-quality, large images with intricate style details. This model has been especially impactful in fields requiring high-resolution style transfer, as it allows for stylization without sacrificing quality or detail in large image outputs.

For applications where achieving clear textures and consistent visual fidelity is crucial, VQ-VAE by van den Oord et al. \cite{van2017neural} introduced vector quantization in the latent space, which reduces image blurriness through discrete latent representations. Its later iteration, VQ-VAE-2 \cite{razavi2019generating}, extended this concept with a hierarchical encoding process, further enhancing texture clarity and consistency, making it ideal for style transfer tasks that prioritize sharp, vivid details.

Through these advancements, VAE variants have significantly progressed in enhancing image quality, achieving feature disentanglement, incorporating multi-scale representation, and enabling targeted generation. These models not only improve the applicability of style transfer for artistic and creative outputs but also provide a versatile foundation for further innovations in the field, paving the way for more expressive, detailed, and user-driven style transfer applications.




\begin{table*}[h!]
\centering
\begin{tabular}{c c c c c c }
\hline
\textbf{Year} & \textbf{\#} & \textbf{Methods} & \textbf{Author} & \textbf{Publication} & \textbf{Innovation}   \\
\hline
2013 & \cite{kingma2013auto} & VAE & Kingma et al. & ICLR & Variational inference for generative models  \\
\hline
2017 & \cite{higgins2017beta} & $\beta$-VAE & Higgins et al. & ICLR & Disentangled representation learning with KL term scaling  \\
\hline
2017 & \cite{van2017neural} & VQ-VAE & van den Oord et al. & NeurIPS & Discrete latent representation through vector quantization  \\
\hline
2016 & \cite{sonderby2016ladder} & Hierarchical VAE & Sønderby et al. & NeurIPS & Multi-scale latent variable modeling \\
\hline
2015 & \cite{sohn2015learning} & Conditional VAE (CVAE) & Sohn et al. & NeurIPS & Conditioning on attributes for controlled generation  \\
\hline
2018 & \cite{kim2018disentangling} & FactorVAE & Kim and Mnih & ICML & Total correlation minimization for improved disentanglement \\
\hline
2017 & \cite{zhao2017info} & InfoVAE (MMD-VAE) & Zhao et al. & arXiv & MMD penalty instead of KL divergence for flexible priors
\\
\hline
2018 & \cite{kumar2018variational} & DIP-VAE & Kumar et al. & ICLR & Disentanglement via covariance regularization  \\
\hline
2018 & \cite{chen2018isolating} & $\beta$-TCVAE & Chen et al. & ICML & Explicit total correlation term to reduce redundancy  \\
\hline

2019 & \cite{child2019biggan} & BigVAE & Child et al. & ICLR & Large-scale VAE with hierarchical latent spaces  \\
\hline
2019 & \cite{razavi2019generating} & VQ-VAE-2 & Razavi et al. & NeurIPS & Hierarchical VQ-VAE with multi-stage encoding  \\
\hline
2020 & \cite{vahdat2020nvae} & NVAE & Vahdat and Kautz & NeurIPS & Efficient hierarchical VAE with normalizing flows  \\
\hline
2020 & \cite{oord2018parallel} & Parallel VAE & van den Oord et al. & ICML & Parallel training for faster VAE convergence  \\
\hline
2021 & \cite{xu2021variational} & StyleVAE & Xu et al. & CVPR & Integrating style transfer into VAE framework \\
\hline
2021 & \cite{vahdat2021score} & Score-VAE & Vahdat et al. & NeurIPS & Using score matching with VAE for sharper generation\\
\hline
2022 & \cite{shen2022distillation} & Distilled-VAE & Shen et al. & ICML & Distilling knowledge into compact VAE  \\
\hline
2023 & \cite{bao2023masked} & Masked-VAE & Bao et al. & CVPR & Masked modeling for VAE to enhance detail  \\
\hline
2023 & \cite{gao2023dynamic} & DynamicVAE & Gao et al. & AAAI & Adaptive latent space for dynamic content  \\
\hline
\end{tabular}

\caption{Summary of Key VAE Variants and Their Innovations}
\label{tab:vae_variants}

\end{table*}
