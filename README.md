<div align="center">

# Awesome Style Transfer

<img src="assets/banner.png" width="800" alt="Style transfer examples">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Style carriers](https://img.shields.io/badge/Style%20carriers-4-42647a)](#taxonomy)
[![Papers](https://img.shields.io/badge/Included%20papers-136-42647a)](#papers)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

[Taxonomy](#taxonomy) · [Coverage](#coverage) · [Papers](#papers) · [Survey data](data/survey-v26/README.md)

</div>

A curated collection of image, video, 3D and dynamic-scene style transfer, organized by how a requested style is acquired, applied and reused. The revised survey uses four primary style carriers and records native generative latents as related mechanisms.

The catalogue contains **136 included publications: 108 core, 24 adjacent and 4 boundary**. [Survey data](data/survey-v26/README.md) provide source-level evidence, protocol coding and the benchmark crosswalk. The [catalogue](data/survey-v26/catalogue.csv) records configuration notes.

## Taxonomy

| Carrier | Deployment interface | Included | Core |
|---|---|---:|---:|
| [Objective-defined style](#objective) | Style specifies a loss, score or guidance objective. | 27 | 27 |
| [Feature-operated style](#feature) | Reference statistics or activations directly transform target features. | 39 | 38 |
| [Parameter-bound style](#parameter) | Retained style-specific weights or tokens serve subsequent content. | 29 | 18 |
| [Encoder-conditioned style](#condition) | A separately encoded reference enters a dedicated conditioning interface. | 33 | 22 |

Labels describe deployment configurations. Meta Networks is Parameter when its generated transformer is retained; the reference-conditioned producer describes acquisition. Native latent context and unresolved hybrids are listed separately.

## Coverage

Strict-core publications, counted once by their primary carrier and output modality.

| Carrier | Image | Video | 3D | 4D | Multiple | Total |
|---|---:|---:|---:|---:|---:|---:|
| Objective-defined style | 7 | 1 | 15 | 3 | 1 | 27 |
| Feature-operated style | 24 | 2 | 7 | 3 | 2 | 38 |
| Parameter-bound style | 13 | 5 | 0 | 0 | 0 | 18 |
| Encoder-conditioned style | 13 | 2 | 6 | 0 | 1 | 22 |
| Hybrid interfaces | 2 | 1 | 0 | 0 | 0 | 3 |

Zero cells describe this catalogue; they do not establish an exhaustive absence in the field.

## Papers

<a id="objective"></a>
### Objective-defined style

Style specifies a loss, score or guidance objective.

| Paper | Year | Output | Scope |
|---|---:|---|---|
| [A neural algorithm of artistic style](https://arxiv.org/pdf/1508.06576v2) | 2015 | Image | Core |
| [Artistic style transfer for videos](https://arxiv.org/pdf/1604.08610v2) | 2016 | Video | Core |
| [Deep photo style transfer](https://arxiv.org/abs/1703.07511) | 2017 | Image | Core |
| [Arbitrary Style Transfer with Deep Feature Reshuffle](https://openaccess.thecvf.com/content_cvpr_2018/html/Gu_Arbitrary_Style_Transfer_CVPR_2018_paper.html) | 2018 | Image | Core |
| [Style transfer by relaxed optimal transport and self-similarity](https://arxiv.org/abs/1904.12785) | 2019 | Image | Core |
| [Arf: Artistic radiance fields](https://arxiv.org/pdf/2206.06360) | 2022 | 3D | Core |
| [CLIPstyler: Image style transfer with a single text condition](https://arxiv.org/abs/2112.00374) | 2022 | Image | Core |
| [Diffusion-based image translation using disentangled style and content representation](https://arxiv.org/abs/2209.15264) | 2022 | Image | Core |
| [SNeRF: Stylized neural implicit representations for 3D scenes](https://arxiv.org/pdf/2207.02363v1) | 2022 | 3D | Core |
| [StyleMesh: Style transfer for indoor 3D scene reconstructions](https://arxiv.org/abs/2112.01530) | 2022 | 3D | Core |
| [Ref-NPR: Reference-Based Non-Photorealistic Radiance Fields for Controllable Scene Stylization](https://arxiv.org/abs/2212.02766) | 2023 | 3D | Core |
| [Transforming Radiance Field With Lipschitz Network for Photorealistic 3D Scene Stylization](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_Transforming_Radiance_Field_With_Lipschitz_Network_for_Photorealistic_3D_Scene_CVPR_2023_paper.pdf) | 2023 | 3D | Core |
| [3D Paintbrush: Local Stylization of 3D Shapes with Cascaded Score Distillation](https://arxiv.org/abs/2311.09571) | 2024 | 3D | Core |
| [NeRF-Art: Text-Driven Neural Radiance Fields Stylization](https://arxiv.org/abs/2212.08070) | 2024 | 3D | Core |
| [S-DyRF: Reference-Based Stylized Radiance Fields for Dynamic Scenes](https://arxiv.org/pdf/2403.06205v3) | 2024 | 4D | Core |
| [Balanced image stylization with style matching score](https://arxiv.org/abs/2503.07601) | 2025 | Image | Core |
| [CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting](https://arxiv.org/abs/2505.22854) | 2025 | Multiple | Core |
| [Fantasystyle: Controllable stylized distillation for 3d gaussian splatting](https://arxiv.org/abs/2508.08136) | 2025 | 3D | Core |
| [GAS-NeRF: Geometry-Aware Stylization of Dynamic Radiance Fields](https://arxiv.org/pdf/2503.08483v1) | 2025 | 4D | Core |
| [Geometry in Style: 3D Stylization via Surface Normal Deformation](https://openaccess.thecvf.com/content/CVPR2025/html/Dinh_Geometry_in_Style_3D_Stylization_via_Surface_Normal_Deformation_CVPR_2025_paper.html) | 2025 | 3D | Core |
| [GT\^ 2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208) | 2025 | 3D | Core |
| [Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization](https://arxiv.org/abs/2503.02009) | 2025 | 3D | Core |
| [SGSST: Scaling Gaussian Splatting Style Transfer](https://arxiv.org/abs/2412.03371) | 2025 | 3D | Core |
| [Stylizedgs: Controllable stylization for 3d gaussian splatting](https://arxiv.org/abs/2404.05220) | 2025 | 3D | Core |
| [DiffStyle3D: Consistent 3D Gaussian Stylization via Attention Optimization](https://arxiv.org/abs/2601.19717) | 2026 | 3D | Core |
| [Geometry-Aware Style Transfer in 3D Gaussian Splatting](https://arxiv.org/html/2606.24144) | 2026 | 3D | Core |
| [Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/pdf/2508.19243v1) | 2026 | 4D | Core |

<a id="feature"></a>
### Feature-operated style

Reference statistics or activations directly transform target features.

| Paper | Year | Output | Scope |
|---|---:|---|---|
| [Arbitrary style transfer in real-time with adaptive instance normalization](https://arxiv.org/pdf/1703.06868v2) | 2017 | Image | Core |
| [Universal style transfer via feature transforms](https://arxiv.org/pdf/1705.08086v2) | 2017 | Image | Core |
| [A closed-form solution to photorealistic image stylization](https://arxiv.org/abs/1802.06474) | 2018 | Image | Core |
| [Avatar-net: Multi-scale zero-shot style transfer by feature decoration](https://arxiv.org/abs/1805.03857) | 2018 | Image | Core |
| [Arbitrary Style Transfer with Style-Attentional Networks](https://arxiv.org/abs/1812.02342) | 2019 | Image | Core |
| [Learning linear transformations for fast image and video style transfer](https://arxiv.org/pdf/1808.04537v1) | 2019 | Multiple | Core |
| [Photorealistic style transfer via wavelet transforms](https://arxiv.org/abs/1903.09760) | 2019 | Image | Core |
| [AdaAttN: Revisit attention mechanism in arbitrary neural style transfer](https://arxiv.org/abs/2108.03647) | 2021 | Image | Core |
| [Arbitrary video style transfer via multi-channel correlation](https://arxiv.org/pdf/2009.08003v2) | 2021 | Video | Core |
| [Artflow: Unbiased image style transfer via reversible neural flows](https://arxiv.org/pdf/2103.16877v2) | 2021 | Image | Core |
| [CCPL: Contrastive coherence preserving loss for versatile style transfer](https://arxiv.org/pdf/2207.04808v4) | 2022 | Multiple | Core |
| [Domain enhanced arbitrary image style transfer via contrastive learning](https://arxiv.org/abs/2205.09542) | 2022 | Image | Core |
| [Exact feature distribution matching for arbitrary style transfer and domain generalization](https://arxiv.org/abs/2203.07740) | 2022 | Image | Core |
| [Stytr2: Image style transfer with transformers](https://arxiv.org/abs/2105.14576) | 2022 | Image | Core |
| [UPST-NeRF: Universal Photorealistic Style Transfer of Neural Radiance Fields for 3D Scene](https://arxiv.org/pdf/2208.07059v2) | 2022 | 3D | Core |
| [CAP-VSTNet: Content affinity preserved versatile style transfer](https://arxiv.org/abs/2303.17867) | 2023 | Image | Core |
| [StyleRF: Zero-Shot 3D Style Transfer of Neural Radiance Fields](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_StyleRF_Zero-Shot_3D_Style_Transfer_of_Neural_Radiance_Fields_CVPR_2023_paper.pdf) | 2023 | 3D | Core |
| [Ctrl-x: Controlling structure and appearance for text-to-image generation without guidance](https://arxiv.org/abs/2406.07540) | 2024 | Image | Core |
| [FPRF: Feed-Forward Photorealistic Style Transfer of Large-Scale 3D Neural Radiance Fields](https://ojs.aaai.org/index.php/AAAI/article/view/28054) | 2024 | 3D | Core |
| [G3DST: Generalizing 3D Style Transfer with Neural Radiance Fields across Scenes and Styles](https://arxiv.org/pdf/2408.13508v1) | 2024 | 3D | Core |
| [Puff-Net: Efficient Style Transfer with Pure Content and Style Feature Fusion Network](https://arxiv.org/abs/2405.19775) | 2024 | Image | Core |
| [Rethink arbitrary style transfer with transformer and contrastive learning](https://arxiv.org/abs/2404.13584) | 2024 | Image | Core |
| [Style aligned image generation via shared attention](https://arxiv.org/pdf/2312.02133v2) | 2024 | Image | Core |
| [Style injection in diffusion: A training-free approach for adapting large-scale diffusion models for style transfer](https://arxiv.org/pdf/2312.09008v2) | 2024 | Image | Core |
| [StyleDyRF: Zero-shot 4D Style Transfer for Dynamic Neural Radiance Fields](https://arxiv.org/pdf/2403.08310v1) | 2024 | 4D | Core |
| [StyleGaussian: Instant 3D style transfer with gaussian splatting](https://arxiv.org/pdf/2403.07807v1) | 2024 | 3D | Core |
| [Training-free consistent text-to-image generation](https://arxiv.org/abs/2402.03286) | 2024 | Image | Adjacent |
| [Z*: Zero-shot Style Transfer via Attention Reweighting](https://openaccess.thecvf.com/content/CVPR2024/html/Deng_Z_Zero-shot_Style_Transfer_via_Attention_Reweighting_CVPR_2024_paper.html) | 2024 | Image | Core |
| [A3GS: Arbitrary Artistic Style into Arbitrary 3D Gaussian Splatting](https://openaccess.thecvf.com/content/ICCV2025/html/Fang_A3GS_Arbitrary_Artistic_Style_into_Arbitrary_3D_Gaussian_Splatting_ICCV_2025_paper.html) | 2025 | 3D | Core |
| [AttenST: A Training-Free Attention-Driven Style Transfer Framework with Pre-Trained Diffusion Models](https://arxiv.org/abs/2503.07307) | 2025 | Image | Core |
| [D2 Styler: Advancing Arbitrary Style Transfer with Discrete Diffusion Methods](https://arxiv.org/abs/2408.03558) | 2025 | Image | Core |
| [DVI: Disentangling Semantic and Visual Identity for Training-Free Personalized Generation](https://arxiv.org/abs/2512.18964) | 2025 | Image | Core |
| [FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting](https://arxiv.org/abs/2503.09635) | 2025 | 3D | Core |
| [SCSA: A Plug-and-Play Semantic Continuous-Sparse Attention for Arbitrary Semantic Style Transfer](https://arxiv.org/abs/2503.04119) | 2025 | Image | Core |
| [SOYO: A Tuning-Free Approach for Video Style Morphing via Style-Adaptive Interpolation in Diffusion Models](https://arxiv.org/abs/2503.06998) | 2025 | Video | Core |
| [StyleSSP: Sampling StartPoint Enhancement for Training-free Diffusion-based Method for Style Transfer](https://arxiv.org/abs/2501.11319) | 2025 | Image | Core |
| [StyleStudio: Text-Driven Style Transfer with Selective Control of Style Elements](https://arxiv.org/pdf/2412.08503v2) | 2025 | Image | Core |
| [ZDySS: Zero-Shot Dynamic Scene Stylization using Gaussian Splatting](https://arxiv.org/abs/2501.03875v1) | 2025 | 4D | Core |
| [4DStyleGaussian: Generalizable 4D Style Transfer with Gaussian Splatting](https://arxiv.org/pdf/2410.10412v1) | 2026 | 4D | Core |

<a id="parameter"></a>
### Parameter-bound style

Retained style-specific weights or tokens serve subsequent content.

| Paper | Year | Output | Scope |
|---|---:|---|---|
| [Perceptual losses for real-time style transfer and super-resolution](https://arxiv.org/pdf/1603.08155v1) | 2016 | Image | Core |
| [Texture networks: Feed-forward synthesis of textures and stylized images](https://arxiv.org/abs/1603.03417) | 2016 | Image | Core |
| [A Learned Representation for Artistic Style](https://arxiv.org/abs/1610.07629) | 2017 | Image | Core |
| [Coherent online video style transfer](https://arxiv.org/pdf/1703.09211v2) | 2017 | Video | Core |
| [Real-time neural style transfer for videos](https://openaccess.thecvf.com/content_cvpr_2017/html/Huang_Real-Time_Neural_Style_CVPR_2017_paper.html) | 2017 | Video | Core |
| [Multi-style generative network for real-time transfer](https://arxiv.org/abs/1703.06953) | 2018 | Image | Core |
| [Neural Style Transfer via Meta Networks](https://openaccess.thecvf.com/content_cvpr_2018/html/Shen_Neural_Style_Transfer_CVPR_2018_paper.html) | 2018 | Image | Core |
| [ReCoNet: Real-time coherent video style transfer network](https://arxiv.org/pdf/1807.01197v2) | 2018 | Video | Core |
| [An image is worth one word: Personalizing text-to-image generation using textual inversion](https://arxiv.org/abs/2208.01618) | 2022 | Image | Boundary |
| [VToonify: Controllable High-Resolution Portrait Video Style Transfer](https://arxiv.org/abs/2209.11224) | 2022 | Video | Core |
| [Break-a-scene: Extracting multiple concepts from a single image](https://arxiv.org/abs/2305.16311) | 2023 | Image | Adjacent |
| [Cones: Concept neurons in diffusion models for customized generation](https://arxiv.org/abs/2303.05125) | 2023 | Image | Core |
| [DreamBooth3D: Subject-Driven Text-to-3D Generation](https://arxiv.org/abs/2303.13508) | 2023 | 3D | Adjacent |
| [Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation](https://arxiv.org/abs/2208.12242) | 2023 | Image | Adjacent |
| [Inversion-Based Style Transfer With Diffusion Models](https://arxiv.org/pdf/2211.13203v3) | 2023 | Image | Core |
| [Key-locked rank one editing for text-to-image personalization](https://arxiv.org/abs/2305.01644) | 2023 | Image | Adjacent |
| [Mix-of-show: Decentralized low-rank adaptation for multi-concept customization of diffusion models](https://arxiv.org/abs/2305.18292) | 2023 | Image | Adjacent |
| [Multi-concept customization of text-to-image diffusion](https://arxiv.org/abs/2212.04488) | 2023 | Image | Adjacent |
| [Prospect: Prompt spectrum for attribute-aware personalization of diffusion models](https://arxiv.org/abs/2305.16225) | 2023 | Image | Adjacent |
| [Styledrop: Text-to-image generation in any style](https://arxiv.org/pdf/2306.00983v1) | 2023 | Image | Core |
| [Styleinv: A temporal style modulated inversion network for unconditional video generation](https://arxiv.org/pdf/2308.16909v1) | 2023 | Video | Core |
| [ZipLoRA: Any Subject in Any Style by Effectively Merging LoRAs](https://arxiv.org/pdf/2311.13600v2) | 2023 | Image | Core |
| [Dreamvideo: Composing your dream videos with customized subject and motion](https://arxiv.org/abs/2312.04433) | 2024 | Video | Adjacent |
| [Implicit style-content separation using b-lora](https://arxiv.org/pdf/2403.14572v2) | 2024 | Image | Core |
| [Magic-me: Identity-specific video customized diffusion](https://arxiv.org/abs/2402.09368) | 2024 | Video | Adjacent |
| [APT: Adaptive Personalized Training for Diffusion Models with Limited Data](https://arxiv.org/abs/2507.02687) | 2025 | Image | Adjacent |
| [ConsisLoRA: Enhancing Content and Style Consistency for LoRA-based Style Transfer](https://arxiv.org/pdf/2503.10614v1) | 2025 | Image | Core |
| [Photodoodle: Learning artistic image editing from few-shot pairwise data](https://arxiv.org/abs/2502.14397) | 2025 | Image | Core |
| [RegionRoute: Regional Style Transfer with Diffusion Model](https://arxiv.org/html/2602.19254) | 2026 | Image | Core |

<a id="condition"></a>
### Encoder-conditioned style

A separately encoded reference enters a dedicated conditioning interface.

| Paper | Year | Output | Scope |
|---|---:|---|---|
| [Exploring the Structure of a Real-time, Arbitrary Neural Artistic Stylization Network](https://arxiv.org/abs/1705.06830) | 2017 | Image | Core |
| [CLIP-NeRF: Text-and-image driven manipulation of neural radiance fields](https://arxiv.org/abs/2112.05139) | 2022 | 3D | Core |
| [StylizedNeRF: Consistent 3D Scene Stylization As Stylized NeRF via 2D-3D Mutual Learning](https://openaccess.thecvf.com/content/CVPR2022/papers/Huang_StylizedNeRF_Consistent_3D_Scene_Stylization_As_Stylized_NeRF_via_2D-3D_CVPR_2022_paper.pdf) | 2022 | 3D | Core |
| [Stylizing 3D Scene via Implicit Representation and HyperNetwork](https://arxiv.org/pdf/2105.13016v3) | 2022 | 3D | Core |
| [Blip-diffusion: Pre-trained subject representation for controllable text-to-image generation and editing](https://arxiv.org/abs/2305.14720) | 2023 | Image | Adjacent |
| [Elite: Encoding visual concepts into textual embeddings for customized text-to-image generation](https://arxiv.org/abs/2302.13848) | 2023 | Image | Adjacent |
| [IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models](https://arxiv.org/pdf/2308.06721v1) | 2023 | Image | Core |
| [Arc2Face: A Foundation Model for ID-Consistent Human Faces](https://arxiv.org/abs/2403.11641) | 2024 | Image | Adjacent |
| [ArtAdapter: Text-to-Image Style Transfer using Multi-Level Style Encoder and Explicit Adaptation](https://arxiv.org/pdf/2312.02109v2) | 2024 | Image | Core |
| [Deadiff: An efficient stylization diffusion model with disentangled representations](https://arxiv.org/pdf/2403.06951v2) | 2024 | Image | Core |
| [DiffStyler: Diffusion-based Localized Image Style Transfer](https://arxiv.org/abs/2403.18461) | 2024 | Image | Core |
| [Instantid: Zero-shot identity-preserving generation in seconds](https://arxiv.org/abs/2401.07519) | 2024 | Image | Adjacent |
| [InstantStyle-Plus: Style Transfer with Content-Preserving in Text-to-Image Generation](https://arxiv.org/pdf/2407.00788v1) | 2024 | Image | Core |
| [InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation](https://arxiv.org/abs/2404.02733v2) | 2024 | Image | Core |
| [Photomaker: Customizing realistic human photos via stacked id embedding](https://arxiv.org/abs/2312.04461) | 2024 | Image | Adjacent |
| [Pulid: Pure and lightning id customization via contrastive alignment](https://arxiv.org/abs/2404.16022) | 2024 | Image | Adjacent |
| [Ssr-encoder: Encoding selective subject representation for subject-driven generation](https://arxiv.org/abs/2312.16272) | 2024 | Image | Adjacent |
| [StyleCrafter: Taming Artistic Video Diffusion with Reference-Augmented Adapter Learning](https://arxiv.org/abs/2312.00330) | 2024 | Video | Core |
| [Stylemamba: State space model for efficient text-driven image style transfer](https://arxiv.org/abs/2405.05027) | 2024 | Image | Core |
| [CSGO: Content-Style Composition in Text-to-Image Generation](https://arxiv.org/abs/2408.16766) | 2025 | Image | Core |
| [Free-lunch color-texture disentanglement for stylized image generation](https://arxiv.org/abs/2503.14275) | 2025 | Image | Core |
| [ID-Consistent, Precise Expression Generation with Blendshape-Guided Diffusion](https://arxiv.org/abs/2510.04706) | 2025 | Image | Adjacent |
| [Nested attention: Semantic-aware attention values for concept personalization](https://arxiv.org/abs/2501.01407) | 2025 | Image | Adjacent |
| [Omni-Attribute: Open-vocabulary Attribute Encoder for Visual Concept Personalization](https://arxiv.org/abs/2512.10955) | 2025 | Image | Adjacent |
| [Styl3R: Instant 3D Stylized Reconstruction for Arbitrary Scenes and Styles](https://papers.nips.cc/paper_files/paper/2025/hash/fa1790d7c3036c691d0b2fb3b9a0ce64-Abstract-Conference.html) | 2025 | 3D | Core |
| [Stylemaster: Stylize your video with artistic generation and translation](https://arxiv.org/pdf/2412.07744v1) | 2025 | Video | Core |
| [Styleshot: A snapshot on any style](https://arxiv.org/pdf/2407.01414v2) | 2025 | Image | Core |
| [Stylos: Multi-View 3D Stylization with Single-Forward Gaussian Splatting](https://arxiv.org/pdf/2509.26455v3) | 2025 | 3D | Core |
| [U-StyDiT: Ultra-high quality artistic style transfer using diffusion transformers](https://arxiv.org/abs/2503.08157) | 2025 | Image | Core |
| [Uso: Unified style and subject-driven generation via disentangled and reward learning](https://arxiv.org/abs/2508.18966) | 2025 | Image | Boundary |
| [AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting](https://arxiv.org/abs/2602.04043) | 2026 | 3D | Core |
| [StyleVAR: Controllable Image Style Transfer via Visual Autoregressive Modeling](https://arxiv.org/html/2604.21052) | 2026 | Image | Core |
| [TeleStyle: Content-Preserving Style Transfer in Images and Videos](https://arxiv.org/pdf/2601.20175v1) | 2026 | Multiple | Core |

<a id="context"></a>
### Generative latent context

Native generative coordinates provide related mechanisms alongside the four carriers.

| Paper | Year | Output | Scope |
|---|---:|---|---|
| [Diverse image-to-image translation via disentangled representations](https://arxiv.org/abs/1808.00948) | 2018 | Image | Boundary |
| [Multimodal unsupervised image-to-image translation](https://arxiv.org/abs/1804.04732) | 2018 | Image | Boundary |
| [Styleclip: Text-driven manipulation of stylegan imagery](https://arxiv.org/abs/2103.17249) | 2021 | Image | Adjacent |
| [Diffusion autoencoders: Toward a meaningful and decodable representation](https://arxiv.org/abs/2111.15640) | 2022 | Image | Adjacent |
| [A Style is Worth One Code: Unlocking Code-to-Style Image Generation with Discrete Style Space](https://arxiv.org/html/2511.10555) | 2026 | Image | Adjacent |

<a id="uncertain"></a>
### Hybrid interfaces

These configurations retain an unresolved primary assignment.

| Paper | Year | Output | Scope |
|---|---:|---|---|
| [Stereoscopic Neural Style Transfer](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Stereoscopic_Neural_Style_CVPR_2018_paper.html) | 2018 | Video | Core |
| [Pastiche Master: Exemplar-Based High-Resolution Portrait Style Transfer](https://arxiv.org/abs/2203.13248) | 2022 | Image | Core |
| [CCST-GAN: Generative Adversarial Networks for Chinese Calligraphy Style Transfer](https://doi.org/10.1109/ICIPMC62364.2024.10586662) | 2024 | Image | Core |

## Survey data

[Evidence guide](data/survey-v26/README.md) · [Paper selection](data/survey-v26/evidence_selection.csv) · [Source observations](data/survey-v26/evidence_register.csv) · [Protocol checks](data/survey-v26/verify_counts.py)

Updated 25 October 2026. Source measurements retain their experimental units.

## 📚 Datasets

<details open>
<summary><b>🖼️ Image Datasets</b></summary>

| Dataset | Year | Size | Description | Link |
|---------|------|------|-------------|------|
| WikiArt | 2018 | 42,129 images | Style, Artist, Genre | [link](https://huggingface.co/datasets/huggan/wikiart) |
| Stylized ImageNet | 2018 | ~134GB | Style Transfer | [link](https://github.com/rgeirhos/Stylized-ImageNet) |
| BAM | 2017 | 2.5M images | Artistic Media | [link](https://bam-dataset.org/) |
| ArtBench-10 | 2022 | 60,000 images | Artwork Benchmark | [link](https://github.com/liaochongyang/ArtBench-10) |
| FFHQ | 2019 | 70,000 images | Human Faces | [link](https://github.com/NVlabs/ffhq-dataset) |
| MetFaces | 2020 | 1,336 images | Artistic Faces | [link](https://github.com/NVlabs/metfaces-dataset) |
| AAHQ | 2021 | 25,000 images | Artistic Faces | [link](https://github.com/onion-liu/aahq-dataset) |
| Ukiyo-e Faces | 2020 | 5,209 images | Aligned Ukiyo-e Faces | [link](https://www.justinpinkney.com/blog/2020/ukiyoe-dataset/) |
| DiffusionDB | 2022 | 14M images | Text-to-image | [link](https://github.com/poloclub/diffusiondb) |
| JourneyDB | 2023 | 4.4M images | Multimodal Vision | [link](https://journeydb.github.io/) |
| StyleShot | 2024 | - | Style Transfer | [link](https://styleshot.github.io/) |
| Danbooru2017 | 2017 | 2.94M images | Anime | [link](https://danbooru.donmai.us/posts?tags=2017) |
| Chinese Style Transfer | 2018 | 1000 content, 100 style | Chinese Painting | [link](https://github.com/lbsswu/Chinese_style_transfer) |
| 4SKST | 2023 | 25 color, 100 sketches | Sketch Style | [link](https://github.com/Chanuku/4skst) |

</details>

<details>
<summary><b>🎬 Video Datasets</b></summary>

| Dataset | Year | Size | Description | Link |
|---------|------|------|-------------|------|
| UADFV | 2018 | 100 videos | Video Style Transfer | [link](https://arxiv.org/abs/1811.00661) |
| FaceForensics++ | 2019 | 6000 videos | Swapped Face | [link](https://github.com/ondyari/FaceForensics) |
| Celeb-DF | 2020 | 408 original videos | DeepFake | [link](https://github.com/yuezunli/celeb-deepfakeforensics) |
| DFDC | 2020 | 100,000 clips | DeepFake Detection | [link](https://www.kaggle.com/c/deepfake-detection-challenge) |
| FFIW-10K | 2021 | 10,000 videos | Face Forgery | [link](https://github.com/tfzhou/FFIW) |
| ForgeryNet | 2021 | 221,247 videos | Forgery Analysis | [link](https://github.com/yinanhe/forgerynet) |

</details>

<details>
<summary><b>🧊 3D / Motion Datasets</b></summary>

| Dataset | Year | Size | Description | Link |
|---------|------|------|-------------|------|
| 100STYLE | 2022 | 4M frames | Stylized Motion Capture | [link](https://zenodo.org/records/8127870) |
| Motiondataset | 2023 | 36,673 frames | 3D Motion | [link](https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset) |

</details>

## 🤝 Contributing

We welcome contributions! When suggesting a paper, please indicate which **style carrier** it belongs to:

- 🎯 **Objective** — style lives only in the loss / score / guidance
- 🧩 **Feature** — direct activation matching, transport, or attention coupling
- 🌀 **Latent** — native generative latent, sampleable without a reference
- ⚙️ **Parameter** — persistent style asset (weights / LoRA / tokens)
- 🔌 **Condition** — reference-encoded standalone style condition

Ways to help:

- 🐛 Report bugs and issues
- 💡 Suggest new papers or resources
- 🔧 Submit pull requests
- ⭐ Star this repository if you find it helpful!

## 📖 Citation

If you find this repository useful for your research, please consider citing:

```bibtex
@article{zhang2025style,
  title={Style transfer: A decade survey},
  author={Zhang, Tianshan and Tang, Hao},
  journal={arXiv preprint arXiv:2506.19278},
  year={2025}
}
```

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=neptune-T/Awesome-Style-Transfer&type=Date)](https://star-history.com/#neptune-T/Awesome-Style-Transfer&Date)

## 🙏 Acknowledgments

Thanks to all researchers and developers who made their work publicly available.

<p align="center">
<img src="assets/impression-sunrise.jpg" width=100%>
</p>

<div align="center">
  <sub>By Monet's Impression of Sunrise</sub>
</div>
