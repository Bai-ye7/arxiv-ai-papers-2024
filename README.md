# 最新AI研究论文摘要集合

本仓库收集了来自arXiv的最新AI研究论文摘要，用于跟踪人工智能领域的最新进展。

## 论文列表

### 1. Robust Hypothesis Generation: LLM-Automated Language Bias for Inductive Logic Programming
**ID:** 2505.21486  
**日期:** 2025/05/27  
**作者:** Jiang, Yichen; Cropper, Andrew  
**摘要:** 归纳逻辑编程（ILP）是一种机器学习方法，它从例子中学习逻辑程序。ILP系统通常需要用户提供语言偏置（language bias），如预定义谓词和类型，以限制假设空间。然而，手动指定语言偏置需要领域专业知识，这限制了ILP的可用性。为了解决这个问题，我们引入了一种新方法，利用大型语言模型（LLMs）自动生成语言偏置。我们的方法，称为LLM-Automated Language Bias（LALB），使用LLMs从自然语言问题描述中提取谓词和类型。我们在多个ILP基准测试中评估了LALB，并表明它可以生成与人工指定的语言偏置相当的语言偏置。我们还表明，LALB在各种LLMs上都表现良好，包括开源和闭源模型。我们的结果表明，LLMs可以用来自动化ILP中的语言偏置生成，从而使ILP更易于使用。

### 2. Policy Induction: Predicting Startup Success via Explainable Memory-Augmented In-Context Learning
**ID:** 2505.21427  
**日期:** 2025/05/27  
**作者:** Jiang, Yichen; Cropper, Andrew  
**摘要:** 预测初创公司的成功对风险投资家和企业家至关重要。然而，现有的方法通常依赖于黑盒模型，缺乏可解释性，或者需要大量的领域专业知识来手动设计特征。为了解决这些挑战，我们提出了一种新的方法，称为政策归纳（Policy Induction），它利用记忆增强的上下文学习来预测初创公司的成功。我们的方法首先从历史数据中学习一组政策（如果-那么规则），然后使用这些政策来预测新初创公司的成功。我们在一个包含10,000多家初创公司的真实数据集上评估了我们的方法，并表明它优于现有的方法，包括基于特征的模型和基于深度学习的方法。此外，我们的方法提供了可解释的预测，使用户能够理解为什么特定的初创公司被预测为成功或失败。我们的结果表明，政策归纳是一种有前途的方法，可用于预测初创公司的成功，并为风险投资决策提供可解释的见解。

### 3. Learning Individual Behavior in Agent-Based Models with Graph Diffusion Networks
**ID:** 2505.21426  
**日期:** 2025/05/27  
**作者:** Cozzi, Francesco; Pangallo, Marco; Perotti, Alan; Panisson, André; Monti, Corrado  
**摘要:** 基于代理的模型（ABMs）是研究复杂系统中涌现属性的强大工具。在ABMs中，代理行为由局部交互和随机规则控制。然而，这些规则通常是不可微分的，限制了基于梯度的优化方法的使用，从而限制了与现实世界数据的集成。我们提出了一种新的框架，通过观察ABM生成的数据来学习任何ABM的可微分替代模型。我们的方法结合了扩散模型来捕捉行为随机性和图神经网络来模拟代理交互。与先前的替代方法不同，我们的方法引入了一个基本转变：不是近似系统级输出，而是直接建模个体代理行为，保留了定义ABMs的去中心化、自下而上的动态。我们在两个ABMs（Schelling的隔离模型和捕食者-猎物生态系统）上验证了我们的方法，表明它复制了个体级别的模式，并准确预测了超出训练范围的涌现动态。我们的结果展示了结合扩散模型和图学习用于数据驱动ABM模拟的潜力。

### 4. Diagnosing and Resolving Cloud Platform Instability with Multi-modal RAG LLMs
**ID:** 2505.21419  
**日期:** 2025/05/27  
**作者:** Wang, Yifan; Birman, Kenneth P.  
**摘要:** 当今的云托管应用程序和服务是复杂的系统，性能或功能不稳定可能有数十或数百个潜在的根本原因。我们的假设是，通过结合现代AI工具的模式匹配能力与自然的多模态RAG LLM接口，可以简化问题识别和解决。ARCA是一个针对这一领域的新型多模态RAG LLM系统。逐步评估表明，ARCA的性能优于最先进的替代方案。

### 5. MRSD: Multi-Resolution Skill Discovery for HRL Agents
**ID:** 2505.21410  
**日期:** 2025/05/27  
**作者:** Sharma, Shashank; Hoffmann, Janina; Namboodiri, Vinay  
**摘要:** 分层强化学习（HRL）依靠抽象技能来有效解决长期任务。虽然现有的技能发现方法自动学习这些技能，但它们仅限于每个任务一种技能。相比之下，人类同时学习和使用细粒度和粗粒度的运动技能。受人类运动控制的启发，我们提出了多分辨率技能发现（MRSD），一个HRL框架，它并行学习不同时间分辨率的多个技能编码器。高级管理器动态选择这些技能，实现随时间变化的自适应控制策略。我们在DeepMind控制套件的任务上评估了MRSD，并表明它优于先前最先进的技能发现和HRL方法，实现了更快的收敛和更高的最终性能。我们的发现强调了在HRL中集成多分辨率技能的好处，为更通用和高效的代理铺平了道路。
