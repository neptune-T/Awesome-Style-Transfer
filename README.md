<div align="center">

# 🎨 Awesome Style Transfer

<p align="center">
  <img src="assets/banner-magritte.png" width="800px">
</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Papers](https://img.shields.io/badge/Papers-177-blue)](https://github.com/00lostin00/Awesome-Style-Transfer)
[![Carriers](https://img.shields.io/badge/Style%20Carriers-4-orangeviolet)](https://github.com/00lostin00/Awesome-Style-Transfer)
[![Update](https://img.shields.io/badge/Update-Regularly-green.svg)](https://github.com/00lostin00/Awesome-Style-Transfer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/00lostin00/Awesome-Style-Transfer?style=social)](https://github.com/00lostin00/Awesome-Style-Transfer)

<p align="center">
    <a href="#taxonomy">Taxonomy</a> |
    <a href="#papers">Papers</a> |
    <a href="#coverage">Coverage</a> |
    <a href="#datasets">Datasets</a> |
    <a href="#contributing">Contributing</a> |
    <a href="#comparison-axes">F1–F3</a>
</p>

</div>

## 🎨 About This Repository

A curated collection of **style transfer** research across **🖼️ images, 🎬 video, 🧊 3D scenes and ⏳ dynamic 4D scenes**, organized by the operational taxonomy in *Style Transfer: A Decade Survey*.

> **Domain tags:** 🖼️ Image · 🎬 Video · 🧊 3D · ⏳ 4D · 🌐 Multiple

**October 2026 update:** four combinable carriers describe how style is acquired and applied. Three comparison axes describe **F1: reuse**, **F2: selective binding** and **F3: consistency**. A deployed configuration can use several carriers; a method can address several axes.

## 🖼️ Style Transfer Examples

<div align="center">
<table>
  <tr>
    <th>Content Image</th>
    <th>Style Image</th>
    <th>Transferred Result</th>
  </tr>
  <tr>
    <td><img src="assets/girl.jpg" width="256" height="144" style="object-fit: cover;"></td>
    <td><img src="assets/meitokonekobasu.jpg" width="256" height="144" style="object-fit: cover;"></td>
    <td><img src="assets/result3.png" width="256" height="144" style="object-fit: cover;"></td>
  </tr>
  <tr>
    <td><em>Disaster Girl</em></td>
    <td><em>となりのトトロ</em></td>
    <td><em>Transferred Result</em></td>
  </tr>
</table>
</div>

<a id="taxonomy"></a>

## 🧭 The Style-Carrier Taxonomy

<div align="center">

| Carrier | Style-bearing operation | Papers |
|---------|-------------------------|:------:|
| **[🎯 Optimization Objectives](#objective)** | Reference-dependent losses, scores or guidance optimize an output or a scene. | **31** |
| **[🧩 Feature Operations](#feature)** | Reference statistics, patches or attention directly transform target activations. | **62** |
| **[⚙️ Parameter Assets](#parameter)** | Fitted or predicted style-specific weights, LoRA updates or tokens are retained for later use. | **30** |
| **[🔌 Encoded Conditions](#condition)** | An encoder supplies reference conditions to a shared generator. | **33** |

</div>

**Combined configurations:** InstantStyle uses condition + feature operations; DiffStyler uses parameter assets + feature injection; StyleGallery uses feature matching + objective guidance; ARF retains a fitted scene after objective-based preparation; StyleDyRF combines canonical features with retained scene parameters. Such papers appear in each applicable carrier list. A training loss alone does not classify the frozen inference model as an objective-based method.

<a id="coverage"></a>

## 📊 Coverage at a Glance

**177 unique publications** selected from the revised manuscript: **51 newly linked papers** and **126 retained entries**. Carrier counts include combined configurations and therefore overlap. Adjacent mechanisms, native generative latents and task-specific studies have separate sections.

| Carrier | 🖼️ Image | 🎬 Video | 🧊 3D | ⏳ 4D | 🌐 Multiple | Total |
|---------|:--------:|:--------:|:-----:|:-----:|:----------:|:-----:|
| 🎯 Optimization Objectives | 10 | 2 | 16 | 3 | — | **31** |
| 🧩 Feature Operations | 43 | 5 | 8 | 4 | 2 | **62** |
| ⚙️ Parameter Assets | 23 | 5 | 1 | 1 | — | **30** |
| 🔌 Encoded Conditions | 22 | 3 | 6 | — | 2 | **33** |

## 📑 Table of Contents

1. [🎯 Optimization Objectives](#objective)
2. [🧩 Feature Operations](#feature)
3. [⚙️ Parameter Assets](#parameter)
4. [🔌 Encoded Conditions](#condition)
5. [🌀 Generative Latent Context](#context)
6. [🔀 Other Combined Interfaces](#hybrid)
7. [🔎 Adjacent Mechanisms](#adjacent)
8. [🖌️ Task-specific Stylization](#tasks)
9. [🧪 F1–F3 Comparison Axes](#comparison-axes)
10. [📚 Datasets](#datasets)
11. [🤝 Contributing](#contributing)

<a id="papers"></a>

## 🗂️ Papers by Style Carrier

<a id="objective"></a>

### 1. 🎯 Optimization Objectives

*Reference-dependent losses, scores or guidance optimize an output or a scene.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| A neural algorithm of artistic style | Preprint | 2015 | 🖼️ | [paper](https://arxiv.org/pdf/1508.06576v2) |
| Artistic Style Transfer for Videos | GCPR | 2016 | 🎬 | [paper](https://arxiv.org/pdf/1604.08610v2) |
| Deep photo style transfer | CVPR | 2017 | 🖼️ | [paper](https://arxiv.org/abs/1703.07511) |
| Arbitrary Style Transfer with Deep Feature Reshuffle | CVPR | 2018 | 🖼️ | [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Gu_Arbitrary_Style_Transfer_CVPR_2018_paper.html) |
| Artistic Style Transfer for Videos and Spherical Images | IJCV | 2018 | 🎬 | [paper](https://arxiv.org/abs/1708.04538) |
| Style transfer by relaxed optimal transport and self-similarity | CVPR | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1904.12785) |
| Arf: Artistic radiance fields | ECCV | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2206.06360) |
| CLIPstyler: Image style transfer with a single text condition | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2112.00374) |
| SNeRF: Stylized neural implicit representations for 3D scenes | ACM TOG | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2207.02363v1) |
| StyleMesh: Style transfer for indoor 3D scene reconstructions | CVPR | 2022 | 🧊 | [paper](https://arxiv.org/abs/2112.01530) |
| Diffusion-based image translation using disentangled style and content representation | ICLR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2209.15264) |
| Ref-NPR: Reference-Based Non-Photorealistic Radiance Fields for Controllable Scene Stylization | CVPR | 2023 | 🧊 | [paper](https://arxiv.org/abs/2212.02766) |
| Transforming Radiance Field With Lipschitz Network for Photorealistic 3D Scene Stylization | CVPR | 2023 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_Transforming_Radiance_Field_With_Lipschitz_Network_for_Photorealistic_3D_Scene_CVPR_2023_paper.pdf) |
| 3D Paintbrush: Local Stylization of 3D Shapes with Cascaded Score Distillation | CVPR | 2024 | 🧊 | [paper](https://arxiv.org/abs/2311.09571) |
| Controllable Style Transfer via Test-time Training of Implicit Neural Representation | Pattern Recognition | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2210.07762) |
| NeRF-Art: Text-Driven Neural Radiance Fields Stylization | TVCG | 2024 | 🧊 | [paper](https://arxiv.org/abs/2212.08070) |
| S-DyRF: Reference-Based Stylized Radiance Fields for Dynamic Scenes | CVPR | 2024 | ⏳ | [paper](https://arxiv.org/pdf/2403.06205v3) |
| Balanced image stylization with style matching score | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.07601) |
| GAS-NeRF: Geometry-Aware Stylization of Dynamic Radiance Fields | Preprint | 2025 | ⏳ | [paper](https://arxiv.org/pdf/2503.08483v1) |
| Geometry in Style: 3D Stylization via Surface Normal Deformation | CVPR | 2025 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Dinh_Geometry_in_Style_3D_Stylization_via_Surface_Normal_Deformation_CVPR_2025_paper.html) |
| Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization | CVPR | 2025 | 🧊 | [paper](https://arxiv.org/abs/2503.02009) |
| SGSST: Scaling Gaussian Splatting Style Transfer | CVPR | 2025 | 🧊 | [paper](https://arxiv.org/abs/2412.03371) |
| Stylizedgs: Controllable stylization for 3d gaussian splatting | TPAMI | 2025 | 🧊 | [paper](https://arxiv.org/abs/2404.05220) |
| Tune-Your-Style: Intensity-tunable 3D Style Transfer with Gaussian Splatting | ICCV | 2025 | 🧊 | [paper](https://arxiv.org/abs/2602.00618) |
| CLeaR: A Unified Framework for Resolving the Leakage--Degradation Dilemma in Style Transfer | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2609.38136) |
| DiffStyle3D: Consistent 3D Gaussian Stylization via Attention Optimization | ICML | 2026 | 🧊 | [paper](https://arxiv.org/abs/2601.19717) |
| Fantasystyle: Controllable stylized distillation for 3d gaussian splatting | AAAI | 2026 | 🧊 | [paper](https://arxiv.org/abs/2508.08136) |
| Geometry-Aware Style Transfer in 3D Gaussian Splatting | ECCV | 2026 | 🧊 | [paper](https://arxiv.org/html/2606.24144) |
| GT2-GS: Geometry-aware Texture Transfer for Gaussian Splatting | AAAI | 2026 | 🧊 | [paper](https://arxiv.org/abs/2505.15208) |
| Style4D-Bench: A Benchmark Suite for 4D Stylization | AAAI | 2026 | ⏳ | [paper](https://arxiv.org/pdf/2508.19243v1) |
| StyleGallery: Training-free and Semantic-aware Personalized Style Transfer from Arbitrary Image References | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2603.10354) |

<a id="feature"></a>

### 2. 🧩 Feature Operations

*Reference statistics, patches or attention directly transform target activations.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Arbitrary style transfer in real-time with adaptive instance normalization | ICCV | 2017 | 🖼️ | [paper](https://arxiv.org/pdf/1703.06868v2) |
| Universal style transfer via feature transforms | NeurIPS | 2017 | 🖼️ | [paper](https://arxiv.org/pdf/1705.08086v2) |
| A closed-form solution to photorealistic image stylization | ECCV | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1802.06474) |
| Avatar-net: Multi-scale zero-shot style transfer by feature decoration | CVPR | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1805.03857) |
| Arbitrary Style Transfer with Style-Attentional Networks | CVPR | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1812.02342) |
| Content and Style Disentanglement for Artistic Style Transfer | ICCV | 2019 | 🖼️ | [paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Kotovenko_Content_and_Style_Disentanglement_for_Artistic_Style_Transfer_ICCV_2019_paper.html) |
| Learning linear transformations for fast image and video style transfer | CVPR | 2019 | 🌐 | [paper](https://arxiv.org/pdf/1808.04537v1) |
| Photorealistic style transfer via wavelet transforms | ICCV | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1903.09760) |
| AdaAttN: Revisit attention mechanism in arbitrary neural style transfer | ICCV | 2021 | 🖼️ | [paper](https://arxiv.org/abs/2108.03647) |
| Arbitrary video style transfer via multi-channel correlation | AAAI | 2021 | 🎬 | [paper](https://arxiv.org/pdf/2009.08003v2) |
| Artflow: Unbiased image style transfer via reversible neural flows | CVPR | 2021 | 🖼️ | [paper](https://arxiv.org/pdf/2103.16877v2) |
| CCPL: Contrastive coherence preserving loss for versatile style transfer | ECCV | 2022 | 🌐 | [paper](https://arxiv.org/pdf/2207.04808v4) |
| Domain enhanced arbitrary image style transfer via contrastive learning | SIGGRAPH | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2205.09542) |
| Exact feature distribution matching for arbitrary style transfer and domain generalization | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2203.07740) |
| Stytr2: Image style transfer with transformers | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2105.14576) |
| UPST-NeRF: Universal Photorealistic Style Transfer of Neural Radiance Fields for 3D Scene | Preprint | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2208.07059v2) |
| A Unified Arbitrary Style Transfer Framework via Adaptive Contrastive Learning | ACM TOG | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2303.12710) |
| AesPA-Net: Aesthetic Pattern-Aware Style Transfer Networks | ICCV | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2307.09724) |
| CAP-VSTNet: Content affinity preserved versatile style transfer | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2303.17867) |
| StyleRF: Zero-Shot 3D Style Transfer of Neural Radiance Fields | CVPR | 2023 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_StyleRF_Zero-Shot_3D_Style_Transfer_of_Neural_Radiance_Fields_CVPR_2023_paper.pdf) |
| AesFA: An Aesthetic Feature-Aware Arbitrary Neural Style Transfer | AAAI | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2312.05928) |
| Ctrl-x: Controlling structure and appearance for text-to-image generation without guidance | NeurIPS | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2406.07540) |
| DiffStyler: Diffusion-based Localized Image Style Transfer | Preprint | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2403.18461) |
| FPRF: Feed-Forward Photorealistic Style Transfer of Large-Scale 3D Neural Radiance Fields | AAAI | 2024 | 🧊 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/28054) |
| G3DST: Generalizing 3D Style Transfer with Neural Radiance Fields across Scenes and Styles | GCPR | 2024 | 🧊 | [paper](https://arxiv.org/pdf/2408.13508v1) |
| InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation | Preprint | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2404.02733v2) |
| Puff-Net: Efficient Style Transfer with Pure Content and Style Feature Fusion Network | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2405.19775) |
| Rethink Arbitrary Style Transfer with Transformer and Contrastive Learning | CVIU | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2404.13584) |
| S2WAT: Image Style Transfer via Hierarchical Vision Transformer Using Strips Window Attention | AAAI | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2210.12381) |
| Style aligned image generation via shared attention | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2312.02133v2) |
| Style injection in diffusion: A training-free approach for adapting large-scale diffusion models for style transfer | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2312.09008v2) |
| StyleDyRF: Zero-shot 4D Style Transfer for Dynamic Neural Radiance Fields | Preprint | 2024 | ⏳ | [paper](https://arxiv.org/pdf/2403.08310v1) |
| StyleGaussian: Instant 3D Style Transfer with Gaussian Splatting | SIGASIA # { Technical Communications} | 2024 | 🧊 | [paper](https://arxiv.org/pdf/2403.07807v1) |
| Z*: Zero-shot Style Transfer via Attention Reweighting | CVPR | 2024 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Deng_Z_Zero-shot_Style_Transfer_via_Attention_Reweighting_CVPR_2024_paper.html) |
| A3GS: Arbitrary Artistic Style into Arbitrary 3D Gaussian Splatting | ICCV | 2025 | 🧊 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Fang_A3GS_Arbitrary_Artistic_Style_into_Arbitrary_3D_Gaussian_Splatting_ICCV_2025_paper.html) |
| AttenST: A Training-Free Attention-Driven Style Transfer Framework with Pre-Trained Diffusion Models | Preprint | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.07307) |
| CSD-VAR: Content-Style Decomposition in Visual Autoregressive Models | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2507.13984) |
| D2Styler: Advancing Arbitrary Style Transfer with Discrete Diffusion Methods | ICPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2408.03558) |
| DVI: Disentangling Semantic and Visual Identity for Training-Free Personalized Generation | Preprint | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2512.18964) |
| FlowStyler: Artistic Video Stylization via Transformation Fields Transports | ICCV | 2025 | 🎬 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_FlowStyler_Artistic_Video_Stylization_via_Transformation_Fields_Transports_ICCV_2025_paper.html) |
| FreeViS: Training-free Video Stylization with Inconsistent References | Preprint | 2025 | 🎬 | [paper](https://arxiv.org/abs/2510.01686) |
| HSI: A Holistic Style Injector for Arbitrary Style Transfer | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2502.04369) |
| Only-Style: Stylistic Consistency in Image Generation without Content Leakage | ICCVW | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2506.09916) |
| SaMam: Style-aware State Space Model for Arbitrary Image Style Transfer | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.15934) |
| SCSA: A Plug-and-Play Semantic Continuous-Sparse Attention for Arbitrary Semantic Style Transfer | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.04119) |
| SOYO: A Tuning-Free Approach for Video Style Morphing via Style-Adaptive Interpolation in Diffusion Models | Preprint | 2025 | 🎬 | [paper](https://arxiv.org/abs/2503.06998) |
| StyleKeeper: Prevent Content Leakage using Negative Visual Query Guidance | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2510.06827) |
| StyleSSP: Sampling StartPoint Enhancement for Training-free Diffusion-based Method for Style Transfer | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2501.11319) |
| StyleStudio: Text-Driven Style Transfer with Selective Control of Style Elements | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/pdf/2412.08503v2) |
| Towards 4D Human Video Stylization | CVIU | 2025 | ⏳ | [paper](https://arxiv.org/abs/2312.04143) |
| ZDySS: Zero-Shot Dynamic Scene Stylization using Gaussian Splatting | Preprint | 2025 | ⏳ | [paper](https://arxiv.org/abs/2501.03875v1) |
| 4DStyleGaussian: Generalizable 4D Style Transfer with Gaussian Splatting | Pattern Recognition | 2026 | ⏳ | [paper](https://arxiv.org/pdf/2410.10412v1) |
| A Training-Free Style-Personalization via SVD-Based Feature Decomposition | CVPR | 2026 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_A_Training-Free_Style-Personalization_via_SVD-Based_Feature_Decomposition_CVPR_2026_paper.html) |
| CleanStyle: Plug-and-Play Style Conditioning Purification for Text-to-Image Stylization | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2602.20721) |
| CLeaR: A Unified Framework for Resolving the Leakage--Degradation Dilemma in Style Transfer | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2609.38136) |
| Disentangling Dual Image References in Frequency Aware Diffusion Models for Personalized Generation | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2610.07684) |
| FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting | IJCV | 2026 | 🧊 | [paper](https://arxiv.org/abs/2503.09635) |
| Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2610.23238) |
| Optimization-Free Style Transfer for 3D Gaussian Splats | WACV | 2026 | 🧊 | [paper](https://arxiv.org/abs/2508.05813) |
| SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2609.21242) |
| StyleGallery: Training-free and Semantic-aware Personalized Style Transfer from Arbitrary Image References | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2603.10354) |
| UniVST: A Unified Framework for Training-free Localized Video Style Transfer | TPAMI | 2026 | 🎬 | [paper](https://arxiv.org/abs/2410.20084) |

<a id="parameter"></a>

### 3. ⚙️ Parameter Assets

*Fitted or predicted style-specific weights, LoRA updates or tokens are retained for later use.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Perceptual losses for real-time style transfer and super-resolution | ECCV | 2016 | 🖼️ | [paper](https://arxiv.org/pdf/1603.08155v1) |
| Texture networks: Feed-forward synthesis of textures and stylized images | ICML | 2016 | 🖼️ | [paper](https://arxiv.org/abs/1603.03417) |
| A Learned Representation for Artistic Style | ICLR | 2017 | 🖼️ | [paper](https://arxiv.org/abs/1610.07629) |
| Coherent online video style transfer | ICCV | 2017 | 🎬 | [paper](https://arxiv.org/pdf/1703.09211v2) |
| Real-time neural style transfer for videos | CVPR | 2017 | 🎬 | [paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Huang_Real-Time_Neural_Style_CVPR_2017_paper.html) |
| Multi-style Generative Network for Real-time Transfer | ECCVW | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1703.06953) |
| Neural Style Transfer via Meta Networks | CVPR | 2018 | 🖼️ | [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Shen_Neural_Style_Transfer_CVPR_2018_paper.html) |
| ReCoNet: Real-time coherent video style transfer network | ACCV | 2018 | 🎬 | [paper](https://arxiv.org/pdf/1807.01197v2) |
| Arf: Artistic radiance fields | ECCV | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2206.06360) |
| Real-Time Portrait Stylization on the Edge | IJCAI # { Demo Track} | 2022 | 🖼️ | [paper](https://www.ijcai.org/proceedings/2022/0856.pdf) |
| VToonify: Controllable High-Resolution Portrait Video Style Transfer | ACM TOG | 2022 | 🎬 | [paper](https://arxiv.org/abs/2209.11224) |
| An image is worth one word: Personalizing text-to-image generation using textual inversion | ICLR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2208.01618) |
| Cones: Concept neurons in diffusion models for customized generation | ICML | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2303.05125) |
| Inversion-Based Style Transfer With Diffusion Models | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2211.13203v3) |
| Specialist Diffusion: Plug-and-Play Sample-Efficient Fine-Tuning of Text-to-Image Diffusion Models To Learn Any Unseen Style | CVPR | 2023 | 🖼️ | [paper](https://github.com/Picsart-AI-Research/Specialist-Diffusion) |
| Styledrop: Text-to-image generation in any style | NeurIPS | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2306.00983v1) |
| Styleinv: A temporal style modulated inversion network for unconditional video generation | ICCV | 2023 | 🎬 | [paper](https://arxiv.org/pdf/2308.16909v1) |
| DiffStyler: Diffusion-based Localized Image Style Transfer | Preprint | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2403.18461) |
| Implicit style-content separation using b-lora | ECCV | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2403.14572v2) |
| StyleDyRF: Zero-shot 4D Style Transfer for Dynamic Neural Radiance Fields | Preprint | 2024 | ⏳ | [paper](https://arxiv.org/pdf/2403.08310v1) |
| ZipLoRA: Any Subject in Any Style by Effectively Merging LoRAs | ECCV | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2311.13600v2) |
| ArtEditor: Learning Customized Instructional Image Editor from Few-Shot Examples | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2502.14397) |
| ConsisLoRA: Enhancing Content and Style Consistency for LoRA-based Style Transfer | Preprint | 2025 | 🖼️ | [paper](https://arxiv.org/pdf/2503.10614v1) |
| K-LoRA: Unlocking Training-Free Fusion of Any Subject and Style LoRAs | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2502.18461) |
| UnZipLoRA: Separating Content and Style from a Single Image | ICCV | 2025 | 🖼️ | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_UnZipLoRA_Separating_Content_and_Style_from_a_Single_Image_ICCV_2025_paper.html) |
| CRAFT-LoRA: Content-Style Personalization via Rank-Constrained Adaptation and Training-Free Fusion | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2602.18936) |
| One-shot Portrait Stylization via Geometric Alignment | WACV | 2026 | 🖼️ | [paper](https://openaccess.thecvf.com/content/WACV2026/papers/Wang_One-shot_Portrait_Stylizaiton_via_Geometric_Alignment_WACV_2026_paper.pdf) |
| RegionRoute: Regional Style Transfer with Diffusion Model | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/html/2602.19254) |
| SplitFlux: Learning to Decouple Content and Style from a Single Image | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2511.15258) |
| Style-GRPO: Semantic-Aware Preference Optimization for Image Style Transfer Guided by Reward Modeling | CVPR | 2026 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Style-GRPO_Semantic-Aware_Preference_Optimization_for_Image_Style_Transfer_Guided_by_CVPR_2026_paper.pdf) |

<a id="condition"></a>

### 4. 🔌 Encoded Conditions

*An encoder supplies reference conditions to a shared generator.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Exploring the Structure of a Real-Time, Arbitrary Neural Artistic Stylization Network | BMVC | 2017 | 🖼️ | [paper](https://arxiv.org/abs/1705.06830) |
| CLIP-NeRF: Text-and-image driven manipulation of neural radiance fields | CVPR | 2022 | 🧊 | [paper](https://arxiv.org/abs/2112.05139) |
| StylizedNeRF: Consistent 3D Scene Stylization As Stylized NeRF via 2D-3D Mutual Learning | CVPR | 2022 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Huang_StylizedNeRF_Consistent_3D_Scene_Stylization_As_Stylized_NeRF_via_2D-3D_CVPR_2022_paper.pdf) |
| Stylizing 3D Scene via Implicit Representation and HyperNetwork | WACV | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2105.13016v3) |
| IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | Preprint | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2308.06721v1) |
| ArtAdapter: Text-to-Image Style Transfer using Multi-Level Style Encoder and Explicit Adaptation | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2312.02109v2) |
| Deadiff: An efficient stylization diffusion model with disentangled representations | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2403.06951v2) |
| InstantStyle-Plus: Style Transfer with Content-Preserving in Text-to-Image Generation | Preprint | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2407.00788v1) |
| InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation | Preprint | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2404.02733v2) |
| StyleCrafter: Taming Stylized Video Diffusion with Reference-Augmented Adapter Learning | ACM TOG | 2024 | 🎬 | [paper](https://arxiv.org/abs/2312.00330) |
| StyleMamba: State Space Model for Efficient Text-driven Image Style Transfer | ECAI | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2405.05027) |
| CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting | NeurIPS | 2025 | 🌐 | [paper](https://arxiv.org/abs/2505.22854) |
| CSGO: Content-Style Composition in Text-to-Image Generation | NeurIPS | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2408.16766) |
| Domain Generalizable Portrait Style Transfer | ICCV | 2025 | 🖼️ | [paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Domain_Generalizable_Portrait_Style_Transfer_ICCV_2025_paper.pdf) |
| Free-lunch color-texture disentanglement for stylized image generation | NeurIPS | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.14275) |
| Less is More: Masking Elements in Image Condition Features Avoids Content Leakages in Style Transfer Diffusion Models | ICLR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2502.07466) |
| OmniStyle2: Learning to Stylize by Learning to Destylize | Preprint | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2509.05970) |
| OmniStyle: Filtering High Quality Style Transfer Data at Scale | CVPR | 2025 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_OmniStyle_Filtering_High_Quality_Style_Transfer_Data_at_Scale_CVPR_2025_paper.pdf) |
| SCFlow: Implicitly Learning Style and Content Disentanglement with Flow Models | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2508.03402) |
| Styl3R: Instant 3D Stylized Reconstruction for Arbitrary Scenes and Styles | NeurIPS | 2025 | 🧊 | [paper](https://papers.nips.cc/paper_files/paper/2025/hash/fa1790d7c3036c691d0b2fb3b9a0ce64-Abstract-Conference.html) |
| Stylemaster: Stylize your video with artistic generation and translation | CVPR | 2025 | 🎬 | [paper](https://arxiv.org/pdf/2412.07744v1) |
| Stylos: Multi-View 3D Stylization with Single-Forward Gaussian Splatting | Preprint | 2025 | 🧊 | [paper](https://arxiv.org/pdf/2509.26455v3) |
| U-StyDiT: Ultra-high quality artistic style transfer using diffusion transformers | Preprint | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.08157) |
| AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting | Preprint | 2026 | 🧊 | [paper](https://arxiv.org/abs/2602.04043) |
| CleanStyle: Plug-and-Play Style Conditioning Purification for Text-to-Image Stylization | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2602.20721) |
| Mixture of Style Experts for Diverse Image Stylization | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2603.16649) |
| SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2609.21242) |
| SCAdapter: Content-Style Disentanglement for Diffusion Style Transfer | WACV | 2026 | 🖼️ | [paper](https://arxiv.org/abs/2512.12963) |
| Styleshot: A snapshot on any style | TPAMI | 2026 | 🖼️ | [paper](https://arxiv.org/pdf/2407.01414v2) |
| StyleVAR: Controllable Image Style Transfer via Visual Autoregressive Modeling | Preprint | 2026 | 🖼️ | [paper](https://arxiv.org/html/2604.21052) |
| TeleStyle: Content-Preserving Style Transfer in Images and Videos | Preprint | 2026 | 🌐 | [paper](https://arxiv.org/pdf/2601.20175v1) |
| Unified Customized Generation by Disentangled Reward Modeling | CVPR | 2026 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Unified_Customized_Generation_by_Disentangled_Reward_Modeling_CVPR_2026_paper.html) |
| VISTA: Triplet-Supervised Video Style Transfer with Diffusion Transformers | Preprint | 2026 | 🎬 | [paper](https://arxiv.org/abs/2605.17312) |

<a id="context"></a>

### 5. 🌀 Generative Latent Context

*Native generative coordinates and motion latents provide context for transferable reference-style interfaces.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Diverse image-to-image translation via disentangled representations | ECCV | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1808.00948) |
| MoCoGAN: Decomposing motion and content for video generation | CVPR | 2018 | 🎬 | [paper](https://arxiv.org/abs/1707.04993) |
| Multimodal Unsupervised Image-to-image Translation | ECCV | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1804.04732) |
| A style-based generator architecture for generative adversarial networks | CVPR | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1812.04948) |
| Analyzing and Improving the Image Quality of StyleGAN | CVPR | 2020 | 🖼️ | [paper](https://arxiv.org/abs/1912.04958) |
| Styleclip: Text-driven manipulation of stylegan imagery | ICCV | 2021 | 🖼️ | [paper](https://arxiv.org/abs/2103.17249) |
| Pastiche Master: Exemplar-Based High-Resolution Portrait Style Transfer | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2203.13248) |
| A Style is Worth One Code: Unlocking Code-to-Style Image Generation with Discrete Style Space | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/html/2511.10555) |

<a id="hybrid"></a>

### 6. 🔀 Other Combined Interfaces

*Stereo stylization combines cross-view correspondence and temporal constraints.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Stereoscopic Neural Style Transfer | CVPR | 2018 | 🎬 | [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Stereoscopic_Neural_Style_CVPR_2018_paper.html) |

<a id="adjacent"></a>

### 7. 🔎 Adjacent Mechanisms

*Personalization, editing and stabilization methods contribute related mechanisms under their own input contracts.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Occlusion-Aware Video Temporal Consistency | ACM MM | 2017 | 🎬 | [paper](https://doi.org/10.1145/3123266.3123363) |
| Learning Long-Term Style-Preserving Blind Video Temporal Consistency | ICME | 2021 | 🎬 | [paper](https://arxiv.org/abs/2103.07278) |
| Break-a-scene: Extracting multiple concepts from a single image | SIGASIA | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.16311) |
| Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2208.12242) |
| Elite: Encoding visual concepts into textual embeddings for customized text-to-image generation | ICCV | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2302.13848) |
| Interactive Control over Temporal Consistency while Stylizing Video Streams | CGF | 2023 | 🎬 | [paper](https://diglib.eg.org/items/c00f2450-d92f-42af-85fd-ac67a0589f0f) |
| Key-locked rank one editing for text-to-image personalization | SIGGRAPH | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.01644) |
| Mix-of-show: Decentralized low-rank adaptation for multi-concept customization of diffusion models | NeurIPS | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.18292) |
| Multi-concept customization of text-to-image diffusion | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2212.04488) |
| Prospect: Prompt spectrum for attribute-aware personalization of diffusion models | ACM TOG | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.16225) |
| Dreamvideo: Composing your dream videos with customized subject and motion | CVPR | 2024 | 🎬 | [paper](https://arxiv.org/abs/2312.04433) |
| Instantid: Zero-shot identity-preserving generation in seconds | Preprint | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2401.07519) |
| Photomaker: Customizing realistic human photos via stacked id embedding | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2312.04461) |
| Ssr-encoder: Encoding selective subject representation for subject-driven generation | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2312.16272) |
| Training-free consistent text-to-image generation | ACM TOG | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2402.03286) |
| Nested attention: Semantic-aware attention values for concept personalization | SIGGRAPH | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2501.01407) |
| StructuReiser: A Structure-preserving Video Stylization Method | CGF | 2025 | 🎬 | [paper](https://arxiv.org/abs/2409.15341) |

<a id="tasks"></a>

### 8. 🖌️ Task-specific Stylization

*Calligraphy, hieroglyphs and preference-driven photography introduce different appearance sources and preservation goals.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| CCST-GAN: Generative Adversarial Networks for Chinese Calligraphy Style Transfer | ICIPMC | 2024 | 🖼️ | [paper](https://doi.org/10.1109/ICIPMC62364.2024.10586662) |
| Neural Style Transfer for Synthesising a Dataset of Ancient Egyptian Hieroglyphs | Preprint | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2504.02163) |
| Learning Personalized Photographic Style from Pairwise User Preferences | CVPR | 2026 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Learning_Personalized_Photographic_Style_from_Pairwise_User_Preferences_CVPR_2026_paper.html) |

<a id="comparison-axes"></a>

## 🧪 F1–F3 Comparison Axes

These are comparison questions rather than exclusive method classes or performance scores. The representative cases below follow the revised manuscript.

- **F1 · Reuse:** what state survives a change of target, style reference, adapter partner, receiving model or scene?
- **F2 · Selective binding:** which reference factors are selected, and where are they assigned in the target?
- **F3 · Consistency:** how is appearance linked across frames, views and dynamic scenes, including disappearance and return?

### F1 · Reuse

| Method | Mechanism | Key condition |
|--------|-----------|---------------|
| [Meta Networks](https://openaccess.thecvf.com/content_cvpr_2018/html/Shen_Neural_Style_Transfer_CVPR_2018_paper.html) | Reference-predicted transformer weights | Reuse across contents within the trained architecture |
| [ZipLoRA](https://arxiv.org/pdf/2311.13600v2) | Optimized merger of separate subject and style LoRAs | Pairwise fitting; reference content may persist |
| [K-LoRA](https://arxiv.org/abs/2502.18461) | Layer-wise adapter selection with timestep scaling | No pairwise fitting after adapter acquisition |
| [CRAFT-LoRA](https://arxiv.org/abs/2602.18936) | Rank-constrained adapters with routed guidance | Training-free fusion after component training |
| [UnZipLoRA](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_UnZipLoRA_Separating_Content_and_Style_from_a_Single_Image_ICCV_2025_paper.html) | Joint subject and style fitting from one image | Direct composition of jointly acquired factors |
| [Kingfisher](https://arxiv.org/abs/2610.23238) | Pair-specific code recombination in a frozen AR model | Less preparation than CSD-VAR; similar output latency |
| [ARF](https://arxiv.org/pdf/2206.06360) | Scene-specific radiance-field optimization | New views reuse fitted state; new scenes require fitting |
| [G3DST](https://arxiv.org/pdf/2408.13508v1) | Style-conditioned parameter prediction | Generalizes to posed scenes without pairwise fitting |
| [FPGS (preparation)](https://arxiv.org/abs/2503.09635) | Feed-forward transformation of Gaussian features | Scene preparation remains; no per-style optimization |
| [Portrait alignment](https://openaccess.thecvf.com/content/WACV2026/papers/Wang_One-shot_Portrait_Stylizaiton_via_Geometric_Alignment_WACV_2026_paper.pdf) | Geometric alignment with fitted portrait adapters | Requires aligned targets and adapter training |
| [Edge portrait stylization](https://www.ijcai.org/proceedings/2022/0856.pdf) | Latency-driven portrait network search | Smartphone inference within learned style domains |

### F2 · Selective binding

| Method | Mechanism | Key condition |
|--------|-----------|---------------|
| [InstantStyle](https://arxiv.org/abs/2404.02733v2) | Content subtraction and selected-block injection | Transfer strength controls reference influence |
| [MaskST](https://arxiv.org/abs/2502.07466) | Text-conditioned masking of reference elements | Selection depends on content text and cluster masks |
| [StyleKeeper](https://arxiv.org/abs/2510.06827) | Negative visual queries and layer selection | Guidance balances style with prompt alignment |
| [Only-Style](https://arxiv.org/abs/2506.09916) | Patch-level leakage detection with adaptive sharing | Suppression depends on detected source content |
| [CleanStyle](https://arxiv.org/abs/2602.20721) | Spectral suppression with negative guidance | Balances leakage reduction with style fidelity |
| [SafeStyle](https://arxiv.org/abs/2609.21242) | Calibrated style-residual injection | Requires calibration sets and a residual budget |
| [CLeaR](https://arxiv.org/abs/2609.38136) | Content projection and calibrated style conditioning | Requires inversion and sampling calibration |
| [Style-GRPO](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Style-GRPO_Semantic-Aware_Preference_Optimization_for_Image_Style_Transfer_Guided_by_CVPR_2026_paper.pdf) | StyleScore-guided GRPO | Text-guided transfer after supervised adaptation |
| [SCFlow](https://arxiv.org/abs/2508.03402) | Invertible merging of crossed style and content latents | Separation measured through latent clustering |
| [CSD-VAR](https://arxiv.org/abs/2507.13984) | Scale alignment with SVD and KV operations | Style control within the autoregressive model |
| [SplitFlux](https://arxiv.org/abs/2511.15258) | Rank-constrained adaptation with saliency gating | Binding depends on adapted Flux blocks |
| [SVD personalization](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_A_Training-Free_Style-Personalization_via_SVD-Based_Feature_Decomposition_CVPR_2026_paper.html) | Feature blending with attention correction | Balances style strength with prompt adherence |
| [StyleGallery](https://arxiv.org/abs/2603.10354) | Semantic region matching with local guidance | Incorrect cluster masks can disrupt transfer |
| [RegionRoute](https://arxiv.org/html/2602.19254) | Text-token routing to target regions | Regional style with protection of unedited areas |

### F3 · Consistency

| Method | Mechanism | Key condition |
|--------|-----------|---------------|
| [Occlusion-aware consistency](https://doi.org/10.1145/3123266.3123363) | Keyframe tracking with color-affine reconstruction | Stability depends on tracked correspondences |
| [Recurrent video filtering](https://arxiv.org/abs/2103.07278) | Recurrent filtering with perceptual supervision | Reduces flicker in already stylized video |
| [FPGS (rendering)](https://arxiv.org/abs/2503.09635) | Scene-level Gaussian stylization before rendering | Shared appearance across reconstructed views |
| [StyleDyRF](https://arxiv.org/pdf/2403.08310v1) | Canonical features deformed with scene geometry | Persistence depends on deformation correspondence |
| [UniVST](https://arxiv.org/abs/2410.20084) | Regional masks with point matching and flow smoothing | Propagation through observed correspondences |
| [FlowStyler](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_FlowStyler_Artistic_Video_Stylization_via_Transformation_Fields_Transports_ICCV_2025_paper.html) | Temporal transport with occlusion-aware lookup | Reduces motion trailing in artistic video |

<a id="datasets"></a>

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

<a id="survey-data"></a>

## 🔎 Survey Data

The [previous v26 data snapshot](https://github.com/00lostin00/Awesome-Style-Transfer/tree/codex/survey-v26-evidence/data/survey-v26) is retained as an archive. Its exclusive carrier counts describe the earlier version; the October 2026 lists above use combinable operations and the revised comparison axes.

<a id="contributing"></a>

## 🤝 Contributing

We welcome contributions! For a paper, include its link, output domain and applicable **objective / feature / parameter / condition** operations. For combined configurations, identify each operation and its retained state. F1, F2 and F3 tags should describe the comparison being addressed.

- 🐛 Report incorrect links or classifications.
- 💡 Suggest papers, datasets or evaluation resources.
- 🔧 Submit a pull request with a short explanation of the deployed configuration.
- ⭐ Star the repository if you find it useful.

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
