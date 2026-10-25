<div align="center">

# 🎨 Awesome Style Transfer

<p align="center">
  <img src="assets/banner-magritte.png" width="800px">
</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Papers](https://img.shields.io/badge/Papers-136-blue)](https://github.com/00lostin00/Awesome-Style-Transfer)
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
    <a href="https://github.com/00lostin00/Awesome-Style-Transfer/tree/codex/survey-v26-evidence/data/survey-v26">Survey data</a>
</p>

</div>

## 🎨 About This Repository

A curated collection of **style transfer** research papers spanning **🖼️ 2D image, 🎬 video, 🧊 3D (NeRF / mesh / point cloud / 3DGS) and ⏳ 4D (dynamic scene) stylization** — organized by the **Style-Carrier Taxonomy** from our survey *Style Transfer: A Decade Survey*.

> **Domain tags:** 🖼️ Image — single-image stylization · 🎬 Video — temporally consistent stylization · 🧊 3D — stylization of 3D representations · ⏳ 4D — dynamic, time-varying 3D scenes · 🌐 Multiple — more than one domain

Instead of grouping papers only by backbone or output domain, we ask:

> **In what form is style-specific information acquired, applied and reused for new content?**

The catalogue contains **136 included publications**: **108 core**, **24 adjacent** and **4 boundary** studies. Four primary carriers organize the transfer interfaces; native generative latents and unresolved hybrid configurations are listed separately.

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

| Carrier | Core idea | Anchors | Papers |
|---------|-----------|---------|:------:|
| 🎯 **[Style as Optimization Objective](#objective)** | Style is applied through a loss, score or guidance objective that optimizes the output or scene. | *Gatys et al. · ARF* | **27** |
| 🧩 **[Style as Feature Operator](#feature)** | Reference statistics or activations directly normalize, match, replace or interact with target features. | *AdaIN · WCT · StyleID* | **39** |
| ⚙️ **[Style as Model Parameters](#parameter)** | Style-specific learned or generated weights, LoRA deltas or tokens are retained for subsequent content. | *Johnson et al. · Meta Networks · LoRA* | **29** |
| 🔌 **[Style as Learned Condition](#condition)** | An external reference is encoded into a standalone style condition consumed through a dedicated generator interface. | *Ghiasi et al. · IP-Adapter* | **33** |

</div>

📌 **Configuration matters:** Meta Networks is Parameter when its generated transformer is retained; the reference-conditioned producer describes acquisition. The catalogue also includes **5 generative-latent context studies** and **3 hybrid configurations**. Full configuration notes are available in the [catalogue](https://github.com/00lostin00/Awesome-Style-Transfer/blob/codex/survey-v26-evidence/data/survey-v26/catalogue.csv).

<a id="coverage"></a>

## 📊 Coverage at a Glance

**Strict-core coverage: 108 studies**, counted once by primary carrier and output representation.

<div align="center">

| Carrier | 🖼️ Image | 🎬 Video | 🧊 3D | ⏳ 4D | 🌐 Multiple | Total |
|---------|:------:|:------:|:---:|:---:|:------:|:---:|
| 🎯 Optimization Objective | 7 | 1 | 15 | 3 | 1 | **27** |
| 🧩 Feature Operator | 24 | 2 | 7 | 3 | 2 | **38** |
| ⚙️ Model Parameters | 13 | 5 | — | — | — | **18** |
| 🔌 Learned Condition | 13 | 2 | 6 | — | 1 | **22** |
| 🔀 Hybrid Interfaces | 2 | 1 | — | — | — | **3** |

</div>

> Counts describe this curated catalogue. A dash indicates no entry in that cell.

## 📑 Table of Contents

1. [🎯 Style as Optimization Objective](#objective) — 27 papers
2. [🧩 Style as Feature Operator](#feature) — 39 papers
3. [⚙️ Style as Model Parameters](#parameter) — 29 papers
4. [🔌 Style as Learned Condition](#condition) — 33 papers
5. [🌀 Generative Latent Context](#context) — 5 papers
6. [🔀 Hybrid and Boundary Interfaces](#uncertain) — 3 papers
7. [📚 Datasets](#datasets)
8. [🔎 Survey Data and Evidence](#survey-data)
9. [🤝 Contributing](#contributing)

<a id="papers"></a>

## 🗂️ Papers by Style Carrier

**Scope markers:** unmarked papers are core studies; † denotes adjacent mechanisms and ‡ denotes scope-boundary studies. Rep follows the domain tags above.

<a id="objective"></a>

### 1. 🎯 Style as Optimization Objective

*Style is applied through a loss, score or guidance objective that optimizes the output or scene.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| A neural algorithm of artistic style | arXiv | 2015 | 🖼️ | [paper](https://arxiv.org/pdf/1508.06576v2) |
| Artistic style transfer for videos | GCPR | 2016 | 🎬 | [paper](https://arxiv.org/pdf/1604.08610v2) |
| Deep photo style transfer | CVPR | 2017 | 🖼️ | [paper](https://arxiv.org/abs/1703.07511) |
| Arbitrary Style Transfer with Deep Feature Reshuffle | CVPR | 2018 | 🖼️ | [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Gu_Arbitrary_Style_Transfer_CVPR_2018_paper.html) |
| Style transfer by relaxed optimal transport and self-similarity | CVPR | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1904.12785) |
| Arf: Artistic radiance fields | ECCV | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2206.06360) |
| CLIPstyler: Image style transfer with a single text condition | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2112.00374) |
| Diffusion-based image translation using disentangled style and content representation | ICLR 2023 | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2209.15264) |
| SNeRF: Stylized neural implicit representations for 3D scenes | ACM TOG | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2207.02363v1) |
| StyleMesh: Style transfer for indoor 3D scene reconstructions | CVPR | 2022 | 🧊 | [paper](https://arxiv.org/abs/2112.01530) |
| Ref-NPR: Reference-Based Non-Photorealistic Radiance Fields for Controllable Scene Stylization | CVPR | 2023 | 🧊 | [paper](https://arxiv.org/abs/2212.02766) |
| Transforming Radiance Field With Lipschitz Network for Photorealistic 3D Scene Stylization | CVPR | 2023 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_Transforming_Radiance_Field_With_Lipschitz_Network_for_Photorealistic_3D_Scene_CVPR_2023_paper.pdf) |
| 3D Paintbrush: Local Stylization of 3D Shapes with Cascaded Score Distillation | CVPR | 2024 | 🧊 | [paper](https://arxiv.org/abs/2311.09571) |
| NeRF-Art: Text-Driven Neural Radiance Fields Stylization | IEEE TVCG | 2024 | 🧊 | [paper](https://arxiv.org/abs/2212.08070) |
| S-DyRF: Reference-Based Stylized Radiance Fields for Dynamic Scenes | CVPR | 2024 | ⏳ | [paper](https://arxiv.org/pdf/2403.06205v3) |
| Balanced image stylization with style matching score | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.07601) |
| CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting | NeurIPS | 2025 | 🌐 | [paper](https://arxiv.org/abs/2505.22854) |
| Fantasystyle: Controllable stylized distillation for 3d gaussian splatting | AAAI 2026 | 2025 | 🧊 | [paper](https://arxiv.org/abs/2508.08136) |
| GAS-NeRF: Geometry-Aware Stylization of Dynamic Radiance Fields | arXiv | 2025 | ⏳ | [paper](https://arxiv.org/pdf/2503.08483v1) |
| Geometry in Style: 3D Stylization via Surface Normal Deformation | CVPR | 2025 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Dinh_Geometry_in_Style_3D_Stylization_via_Surface_Normal_Deformation_CVPR_2025_paper.html) |
| GT²-GS: Geometry-aware Texture Transfer for Gaussian Splatting | arXiv | 2025 | 🧊 | [paper](https://arxiv.org/abs/2505.15208) |
| Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization | CVPR | 2025 | 🧊 | [paper](https://arxiv.org/abs/2503.02009) |
| SGSST: Scaling Gaussian Splatting Style Transfer | CVPR | 2025 | 🧊 | [paper](https://arxiv.org/abs/2412.03371) |
| Stylizedgs: Controllable stylization for 3d gaussian splatting | TPAMI | 2025 | 🧊 | [paper](https://arxiv.org/abs/2404.05220) |
| DiffStyle3D: Consistent 3D Gaussian Stylization via Attention Optimization | arXiv | 2026 | 🧊 | [paper](https://arxiv.org/abs/2601.19717) |
| Geometry-Aware Style Transfer in 3D Gaussian Splatting | ECCV | 2026 | 🧊 | [paper](https://arxiv.org/html/2606.24144) |
| Style4D-Bench: A Benchmark Suite for 4D Stylization | AAAI | 2026 | ⏳ | [paper](https://arxiv.org/pdf/2508.19243v1) |

<a id="feature"></a>

### 2. 🧩 Style as Feature Operator

*Reference statistics or activations directly normalize, match, replace or interact with target features.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Arbitrary style transfer in real-time with adaptive instance normalization | ICCV | 2017 | 🖼️ | [paper](https://arxiv.org/pdf/1703.06868v2) |
| Universal style transfer via feature transforms | NeurIPS | 2017 | 🖼️ | [paper](https://arxiv.org/pdf/1705.08086v2) |
| A closed-form solution to photorealistic image stylization | ECCV | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1802.06474) |
| Avatar-net: Multi-scale zero-shot style transfer by feature decoration | CVPR | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1805.03857) |
| Arbitrary Style Transfer with Style-Attentional Networks | CVPR | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1812.02342) |
| Learning linear transformations for fast image and video style transfer | CVPR | 2019 | 🌐 | [paper](https://arxiv.org/pdf/1808.04537v1) |
| Photorealistic style transfer via wavelet transforms | ICCV | 2019 | 🖼️ | [paper](https://arxiv.org/abs/1903.09760) |
| AdaAttN: Revisit attention mechanism in arbitrary neural style transfer | ICCV | 2021 | 🖼️ | [paper](https://arxiv.org/abs/2108.03647) |
| Arbitrary video style transfer via multi-channel correlation | ICCV | 2021 | 🎬 | [paper](https://arxiv.org/pdf/2009.08003v2) |
| Artflow: Unbiased image style transfer via reversible neural flows | CVPR | 2021 | 🖼️ | [paper](https://arxiv.org/pdf/2103.16877v2) |
| CCPL: Contrastive coherence preserving loss for versatile style transfer | ECCV | 2022 | 🌐 | [paper](https://arxiv.org/pdf/2207.04808v4) |
| Domain enhanced arbitrary image style transfer via contrastive learning | SIGGRAPH | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2205.09542) |
| Exact feature distribution matching for arbitrary style transfer and domain generalization | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2203.07740) |
| Stytr2: Image style transfer with transformers | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2105.14576) |
| UPST-NeRF: Universal Photorealistic Style Transfer of Neural Radiance Fields for 3D Scene | arXiv | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2208.07059v2) |
| CAP-VSTNet: Content affinity preserved versatile style transfer | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2303.17867) |
| StyleRF: Zero-Shot 3D Style Transfer of Neural Radiance Fields | CVPR | 2023 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_StyleRF_Zero-Shot_3D_Style_Transfer_of_Neural_Radiance_Fields_CVPR_2023_paper.pdf) |
| Ctrl-x: Controlling structure and appearance for text-to-image generation without guidance | NeurIPS | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2406.07540) |
| FPRF: Feed-Forward Photorealistic Style Transfer of Large-Scale 3D Neural Radiance Fields | AAAI | 2024 | 🧊 | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/28054) |
| G3DST: Generalizing 3D Style Transfer with Neural Radiance Fields across Scenes and Styles | GCPR | 2024 | 🧊 | [paper](https://arxiv.org/pdf/2408.13508v1) |
| Puff-Net: Efficient Style Transfer with Pure Content and Style Feature Fusion Network | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2405.19775) |
| Rethink arbitrary style transfer with transformer and contrastive learning | CVIU | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2404.13584) |
| Style aligned image generation via shared attention | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2312.02133v2) |
| Style injection in diffusion: A training-free approach for adapting large-scale diffusion models for style transfer | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2312.09008v2) |
| StyleDyRF: Zero-shot 4D Style Transfer for Dynamic Neural Radiance Fields | arXiv | 2024 | ⏳ | [paper](https://arxiv.org/pdf/2403.08310v1) |
| StyleGaussian: Instant 3D style transfer with gaussian splatting | SIGGRAPH Asia | 2024 | 🧊 | [paper](https://arxiv.org/pdf/2403.07807v1) |
| Training-free consistent text-to-image generation † | ACM TOG | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2402.03286) |
| Z*: Zero-shot Style Transfer via Attention Reweighting | CVPR | 2024 | 🖼️ | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Deng_Z_Zero-shot_Style_Transfer_via_Attention_Reweighting_CVPR_2024_paper.html) |
| A3GS: Arbitrary Artistic Style into Arbitrary 3D Gaussian Splatting | ICCV | 2025 | 🧊 | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Fang_A3GS_Arbitrary_Artistic_Style_into_Arbitrary_3D_Gaussian_Splatting_ICCV_2025_paper.html) |
| AttenST: A Training-Free Attention-Driven Style Transfer Framework with Pre-Trained Diffusion Models | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.07307) |
| D2 Styler: Advancing Arbitrary Style Transfer with Discrete Diffusion Methods | ICPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2408.03558) |
| DVI: Disentangling Semantic and Visual Identity for Training-Free Personalized Generation | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2512.18964) |
| FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting | IJCV 2026 | 2025 | 🧊 | [paper](https://arxiv.org/abs/2503.09635) |
| SCSA: A Plug-and-Play Semantic Continuous-Sparse Attention for Arbitrary Semantic Style Transfer | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.04119) |
| SOYO: A Tuning-Free Approach for Video Style Morphing via Style-Adaptive Interpolation in Diffusion Models | arXiv | 2025 | 🎬 | [paper](https://arxiv.org/abs/2503.06998) |
| StyleSSP: Sampling StartPoint Enhancement for Training-free Diffusion-based Method for Style Transfer | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2501.11319) |
| StyleStudio: Text-Driven Style Transfer with Selective Control of Style Elements | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/pdf/2412.08503v2) |
| ZDySS: Zero-Shot Dynamic Scene Stylization using Gaussian Splatting | Preprint | 2025 | ⏳ | [paper](https://arxiv.org/abs/2501.03875v1) |
| 4DStyleGaussian: Generalizable 4D Style Transfer with Gaussian Splatting | Pattern Recognition | 2026 | ⏳ | [paper](https://arxiv.org/pdf/2410.10412v1) |

<a id="parameter"></a>

### 3. ⚙️ Style as Model Parameters

*Style-specific learned or generated weights, LoRA deltas or tokens are retained for subsequent content.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Perceptual losses for real-time style transfer and super-resolution | ECCV | 2016 | 🖼️ | [paper](https://arxiv.org/pdf/1603.08155v1) |
| Texture networks: Feed-forward synthesis of textures and stylized images | ICML | 2016 | 🖼️ | [paper](https://arxiv.org/abs/1603.03417) |
| A Learned Representation for Artistic Style | ICLR | 2017 | 🖼️ | [paper](https://arxiv.org/abs/1610.07629) |
| Coherent online video style transfer | ICCV | 2017 | 🎬 | [paper](https://arxiv.org/pdf/1703.09211v2) |
| Real-time neural style transfer for videos | CVPR | 2017 | 🎬 | [paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Huang_Real-Time_Neural_Style_CVPR_2017_paper.html) |
| Multi-style generative network for real-time transfer | ECCV Workshops | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1703.06953) |
| Neural Style Transfer via Meta Networks | CVPR | 2018 | 🖼️ | [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Shen_Neural_Style_Transfer_CVPR_2018_paper.html) |
| ReCoNet: Real-time coherent video style transfer network | ECCV | 2018 | 🎬 | [paper](https://arxiv.org/pdf/1807.01197v2) |
| An image is worth one word: Personalizing text-to-image generation using textual inversion ‡ | ICLR 2023 | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2208.01618) |
| VToonify: Controllable High-Resolution Portrait Video Style Transfer | ACM TOG | 2022 | 🎬 | [paper](https://arxiv.org/abs/2209.11224) |
| Break-a-scene: Extracting multiple concepts from a single image † | SIGGRAPH Asia | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.16311) |
| Cones: Concept neurons in diffusion models for customized generation | ICML | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2303.05125) |
| DreamBooth3D: Subject-Driven Text-to-3D Generation † | ICCV | 2023 | 🧊 | [paper](https://arxiv.org/abs/2303.13508) |
| Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation † | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2208.12242) |
| Inversion-Based Style Transfer With Diffusion Models | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2211.13203v3) |
| Key-locked rank one editing for text-to-image personalization † | SIGGRAPH | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.01644) |
| Mix-of-show: Decentralized low-rank adaptation for multi-concept customization of diffusion models † | NeurIPS | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.18292) |
| Multi-concept customization of text-to-image diffusion † | CVPR | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2212.04488) |
| Prospect: Prompt spectrum for attribute-aware personalization of diffusion models † | ACM TOG | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.16225) |
| Styledrop: Text-to-image generation in any style | arXiv | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2306.00983v1) |
| Styleinv: A temporal style modulated inversion network for unconditional video generation | ICCV | 2023 | 🎬 | [paper](https://arxiv.org/pdf/2308.16909v1) |
| ZipLoRA: Any Subject in Any Style by Effectively Merging LoRAs | ECCV 2024 | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2311.13600v2) |
| Dreamvideo: Composing your dream videos with customized subject and motion † | CVPR | 2024 | 🎬 | [paper](https://arxiv.org/abs/2312.04433) |
| Implicit style-content separation using b-lora | ECCV | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2403.14572v2) |
| Magic-me: Identity-specific video customized diffusion † | ECCV | 2024 | 🎬 | [paper](https://arxiv.org/abs/2402.09368) |
| APT: Adaptive Personalized Training for Diffusion Models with Limited Data † | CVPR | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2507.02687) |
| ConsisLoRA: Enhancing Content and Style Consistency for LoRA-based Style Transfer | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/pdf/2503.10614v1) |
| Photodoodle: Learning artistic image editing from few-shot pairwise data | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2502.14397) |
| RegionRoute: Regional Style Transfer with Diffusion Model | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/html/2602.19254) |

<a id="condition"></a>

### 4. 🔌 Style as Learned Condition

*An external reference is encoded into a standalone style condition consumed through a dedicated generator interface.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Exploring the Structure of a Real-time, Arbitrary Neural Artistic Stylization Network | BMVC | 2017 | 🖼️ | [paper](https://arxiv.org/abs/1705.06830) |
| CLIP-NeRF: Text-and-image driven manipulation of neural radiance fields | CVPR | 2022 | 🧊 | [paper](https://arxiv.org/abs/2112.05139) |
| StylizedNeRF: Consistent 3D Scene Stylization As Stylized NeRF via 2D-3D Mutual Learning | CVPR | 2022 | 🧊 | [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Huang_StylizedNeRF_Consistent_3D_Scene_Stylization_As_Stylized_NeRF_via_2D-3D_CVPR_2022_paper.pdf) |
| Stylizing 3D Scene via Implicit Representation and HyperNetwork | WACV | 2022 | 🧊 | [paper](https://arxiv.org/pdf/2105.13016v3) |
| Blip-diffusion: Pre-trained subject representation for controllable text-to-image generation and editing † | NeurIPS | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2305.14720) |
| Elite: Encoding visual concepts into textual embeddings for customized text-to-image generation † | ICCV | 2023 | 🖼️ | [paper](https://arxiv.org/abs/2302.13848) |
| IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | arXiv | 2023 | 🖼️ | [paper](https://arxiv.org/pdf/2308.06721v1) |
| Arc2Face: A Foundation Model for ID-Consistent Human Faces † | ECCV | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2403.11641) |
| ArtAdapter: Text-to-Image Style Transfer using Multi-Level Style Encoder and Explicit Adaptation | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2312.02109v2) |
| Deadiff: An efficient stylization diffusion model with disentangled representations | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2403.06951v2) |
| DiffStyler: Diffusion-based Localized Image Style Transfer | arXiv | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2403.18461) |
| Instantid: Zero-shot identity-preserving generation in seconds † | arXiv | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2401.07519) |
| InstantStyle-Plus: Style Transfer with Content-Preserving in Text-to-Image Generation | arXiv | 2024 | 🖼️ | [paper](https://arxiv.org/pdf/2407.00788v1) |
| InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation | arXiv | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2404.02733v2) |
| Photomaker: Customizing realistic human photos via stacked id embedding † | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2312.04461) |
| Pulid: Pure and lightning id customization via contrastive alignment † | NeurIPS | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2404.16022) |
| Ssr-encoder: Encoding selective subject representation for subject-driven generation † | CVPR | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2312.16272) |
| StyleCrafter: Taming Artistic Video Diffusion with Reference-Augmented Adapter Learning | ACM TOG | 2024 | 🎬 | [paper](https://arxiv.org/abs/2312.00330) |
| Stylemamba: State space model for efficient text-driven image style transfer | ECAI | 2024 | 🖼️ | [paper](https://arxiv.org/abs/2405.05027) |
| CSGO: Content-Style Composition in Text-to-Image Generation | NeurIPS | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2408.16766) |
| Free-lunch color-texture disentanglement for stylized image generation | NeurIPS | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.14275) |
| ID-Consistent, Precise Expression Generation with Blendshape-Guided Diffusion † | ICCV | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2510.04706) |
| Nested attention: Semantic-aware attention values for concept personalization † | SIGGRAPH | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2501.01407) |
| Omni-Attribute: Open-vocabulary Attribute Encoder for Visual Concept Personalization † | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2512.10955) |
| Styl3R: Instant 3D Stylized Reconstruction for Arbitrary Scenes and Styles | NeurIPS | 2025 | 🧊 | [paper](https://papers.nips.cc/paper_files/paper/2025/hash/fa1790d7c3036c691d0b2fb3b9a0ce64-Abstract-Conference.html) |
| Stylemaster: Stylize your video with artistic generation and translation | CVPR | 2025 | 🎬 | [paper](https://arxiv.org/pdf/2412.07744v1) |
| Styleshot: A snapshot on any style | TPAMI | 2025 | 🖼️ | [paper](https://arxiv.org/pdf/2407.01414v2) |
| Stylos: Multi-View 3D Stylization with Single-Forward Gaussian Splatting | arXiv | 2025 | 🧊 | [paper](https://arxiv.org/pdf/2509.26455v3) |
| U-StyDiT: Ultra-high quality artistic style transfer using diffusion transformers | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2503.08157) |
| Uso: Unified style and subject-driven generation via disentangled and reward learning ‡ | arXiv | 2025 | 🖼️ | [paper](https://arxiv.org/abs/2508.18966) |
| AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting | arXiv | 2026 | 🧊 | [paper](https://arxiv.org/abs/2602.04043) |
| StyleVAR: Controllable Image Style Transfer via Visual Autoregressive Modeling | arXiv | 2026 | 🖼️ | [paper](https://arxiv.org/html/2604.21052) |
| TeleStyle: Content-Preserving Style Transfer in Images and Videos | arXiv | 2026 | 🌐 | [paper](https://arxiv.org/pdf/2601.20175v1) |

<a id="context"></a>

### 5. 🌀 Generative Latent Context

*Native generative latents supply related appearance and motion mechanisms alongside the four primary carriers.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Diverse image-to-image translation via disentangled representations ‡ | ECCV | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1808.00948) |
| Multimodal unsupervised image-to-image translation ‡ | ECCV | 2018 | 🖼️ | [paper](https://arxiv.org/abs/1804.04732) |
| Styleclip: Text-driven manipulation of stylegan imagery † | ICCV | 2021 | 🖼️ | [paper](https://arxiv.org/abs/2103.17249) |
| Diffusion autoencoders: Toward a meaningful and decodable representation † | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2111.15640) |
| A Style is Worth One Code: Unlocking Code-to-Style Image Generation with Discrete Style Space † | CVPR | 2026 | 🖼️ | [paper](https://arxiv.org/html/2511.10555) |

<a id="uncertain"></a>

### 6. 🔀 Hybrid and Boundary Interfaces

*The recorded configuration combines interfaces for which a unique primary carrier remains unresolved.*

| Paper | Venue | Year | Rep | Link |
|-------|-------|:----:|:---:|------|
| Stereoscopic Neural Style Transfer | CVPR | 2018 | 🎬 | [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Stereoscopic_Neural_Style_CVPR_2018_paper.html) |
| Pastiche Master: Exemplar-Based High-Resolution Portrait Style Transfer | CVPR | 2022 | 🖼️ | [paper](https://arxiv.org/abs/2203.13248) |
| CCST-GAN: Generative Adversarial Networks for Chinese Calligraphy Style Transfer | ICIPMC | 2024 | 🖼️ | [paper](https://doi.org/10.1109/ICIPMC62364.2024.10586662) |

<a id="survey-data"></a>

## 🔎 Survey Data and Evidence

[📋 Catalogue](https://github.com/00lostin00/Awesome-Style-Transfer/blob/codex/survey-v26-evidence/data/survey-v26/catalogue.csv) · [📑 Paper Selection](https://github.com/00lostin00/Awesome-Style-Transfer/blob/codex/survey-v26-evidence/data/survey-v26/evidence_selection.csv) · [🔍 Source Observations](https://github.com/00lostin00/Awesome-Style-Transfer/blob/codex/survey-v26-evidence/data/survey-v26/evidence_register.csv) · [📖 Data Guide](https://github.com/00lostin00/Awesome-Style-Transfer/blob/codex/survey-v26-evidence/data/survey-v26/README.md)

The companion data retain source versions, page/table locations and protocol coding for **192 source observations from 39 studies**. [Verification script](https://github.com/00lostin00/Awesome-Style-Transfer/blob/codex/survey-v26-evidence/data/survey-v26/verify_counts.py).

Updated 25 October 2026.

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

<a id="contributing"></a>
<a id="contributing"></a>

## 🤝 Contributing

We welcome contributions! When suggesting a paper, please indicate which **style carrier** it belongs to:

- 🎯 **Objective** — style lives only in the loss / score / guidance
- 🧩 **Feature** — direct activation matching, transport, or attention coupling
- ⚙️ **Parameter** — persistent style asset (weights / LoRA / tokens)
- 🔌 **Condition** — reference-encoded standalone style condition

Native generative latents can be suggested as **🌀 contextual mechanisms**, and mixed interfaces as **🔀 hybrid configurations**.

Native generative latents can be suggested as **🌀 contextual mechanisms**, and mixed interfaces as **🔀 hybrid configurations**.

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
