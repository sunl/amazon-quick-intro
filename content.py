"""Slide content, narration and sources for the Amazon Quick introduction deck.

Every slide lists the official AWS pages its facts come from (SRC keys); build_deck.py prints
them as clickable links in the slide footer. Narration ("say") is used for the speaker notes and
the video; a (key, text) tuple highlights the element with that key while the text is spoken.
"""
FOOTER = "资料截至 2026-10-31（北京时间）；桌面版按 2026-11-03、套餐按 2026-11-05 的英文文档复核 · 功能、区域与价格以 AWS 官方文档和定价页为准"

D = "https://docs.aws.amazon.com/quick/latest/userguide/"
WN = "https://aws.amazon.com/about-aws/whats-new/"
ML = "https://aws.amazon.com/blogs/machine-learning/"

SRC = {
    # overview, plans
    "whatis": ("What is Amazon Quick?", D + "what-is.html"),
    "how": ("How Amazon Quick works", D + "how-quicksuite-works.html"),
    "history": ("Document history", D + "doc-history.html"),
    "pricing": ("Amazon Quick 定价", "https://aws.amazon.com/quick/pricing/"),
    "plans": ("Free, Plus, and Max plans", D + "standalone-plans.html"),
    "usage": ("Free/Plus/Max usage limits", D + "standalone-usage.html"),
    "signup": ("Signing up through the AWS Console", D + "signing-up.html"),
    "regions": ("Supported Regions", D + "regions.html"),
    "acct": ("Account structure and Regions", D + "account-structure-regions.html"),
    "outbound": ("Outbound connections", D + "outbound-connections.html"),
    "billing": ("Understanding user billing", D + "understanding-quick-user-billing.html"),
    # chat, agents, spaces
    "chat": ("Using Amazon Quick chat", D + "using-quick-chat.html"),
    "explain": ("Chat explanations", D + "chat-explanations.html"),
    "docgen": ("Document and visual creation", D + "document-and-visual-creation.html"),
    "agents": ("Working with chat agents", D + "working-with-agents.html"),
    "custom_agents": ("Custom chat agents", D + "custom-agents.html"),
    "agent_bp": ("Custom chat agent context configuration", D + "agent-knowledge-sources-best-practices.html"),
    "spaces": ("Working with spaces", D + "working-with-spaces.html"),
    "spaces_manage": ("Managing spaces", D + "managing-spaces.html"),
    "brand": ("Brand assets", D + "brand-assets-desktop.html"),
    # Quick Sight
    "sight": ("Amazon Quick Sight", D + "quick-bi.html"),
    "topics": ("Topics", D + "topics.html"),
    "topics_rel": ("Topic relationships", D + "topics-relationships.html"),
    "topics_ci": ("Topic custom instructions", D + "topics-custom-instructions.html"),
    "dash_qa": ("Dashboard Q&A", D + "dashboard-qa.html"),
    "gen_analysis": ("Generating an analysis", D + "generating-an-analysis.html"),
    "scenarios": ("Scenarios", D + "scenarios-create.html"),
    "stories": ("Data stories", D + "working-with-stories-create.html"),
    "enrich": ("Dataset enrichment", D + "dataset-enrichment.html"),
    "embed": ("Embedded analytics", D + "embedded-analytics.html"),
    # Research, Flows, Automate
    "research": ("Using Amazon Quick Research", D + "using-amazon-quick-research.html"),
    "research_obj": ("Research objective", D + "enter-research-objective.html"),
    "research_mat": ("Research materials", D + "select-research-materials.html"),
    "third_party": ("Third party data", D + "third-party-data.html"),
    "automations": ("Choosing Flows or Automate", D + "using-amazon-quick-automations.html"),
    "flows": ("Using Amazon Quick Flows", D + "using-amazon-quick-flows.html"),
    "flows_create": ("Creating flows", D + "creating-flows.html"),
    "flows_steps": ("AI response steps", D + "ai-response-steps.html"),
    "flows_sched": ("Schedules in Quick Flows", D + "schedules-in-quick-flows.html"),
    "automate": ("Using Amazon Quick Automate", D + "using-amazon-quick-automate.html"),
    "automate_build": ("Building automations", D + "building-automations.html"),
    "automate_orch": ("Orchestration actions", D + "actions-orchestration.html"),
    "automate_deploy": ("Deploying automations", D + "deploying-automations.html"),
    "automate_monitor": ("Monitoring performance", D + "monitoring-performance.html"),
}
SRC.update({
    # Apps, desktop, mobile
    "apps": ("Apps in Amazon Quick", D + "using-amazon-quick-apps.html"),
    "apps_build": ("What you can build", D + "what-you-can-build.html"),
    "apps_data": ("Connecting to datasets", D + "connecting-datasets-apps.html"),
    "apps_sec": ("Apps security and sandbox", D + "security-sandbox-apps.html"),
    "apps_tips": ("Apps tips and best practices", D + "tips-best-practices-apps.html"),
    "desktop": ("What is Amazon Quick on desktop?", D + "what-is-desktop.html"),
    "feed": ("Activity feed", D + "activity-feed-desktop.html"),
    "mission": ("Mission Control", D + "mission-control-desktop.html"),
    "skills": ("Skills", D + "skills-desktop.html"),
    "memories": ("Memories", D + "memories-desktop.html"),
    "kg": ("Knowledge graph", D + "knowledge-graph-desktop.html"),
    "knowledge_desktop": ("Knowledge (desktop)", D + "knowledge-desktop.html"),
    "mobile": ("Mobile feature availability", D + "mobile-feature-availability.html"),
    # integrations, extensions
    "integrations": ("Work with integrations", D + "working-with-integrations.html"),
    "supported_int": ("Supported integrations", D + "supported-integrations.html"),
    "kb": ("Knowledge bases", D + "knowledge-base-integrations.html"),
    "acl_bp": ("ACL best practices for knowledge bases", D + "acl-best-practices-kb.html"),
    "actions_how": ("How connectors work", D + "int-actions-how-it-works.html"),
    "tool_perm": ("Connector tool permissions", D + "connector-tool-permissions.html"),
    "mcp": ("MCP integration", D + "mcp-integration.html"),
    "registry": ("AWS Agent Registry integration", D + "aws-agent-registry-integration.html"),
    "byoi": ("Bring your own Amazon Q Business index", D + "quick-byoa.html"),
    "byo_bedrock": ("Bring your own Bedrock knowledge base", D + "quick-byo-bedrock-kb.html"),
    "extensions": ("Extensions", D + "working-with-extensions-detail.html"),
    "browser_ext": ("Browser extension", D + "browser-extension-user-guide.html"),
    "outlook_ext": ("Outlook extension", D + "outlook-extension-guide.html"),
    "excel_ext": ("Excel extension", D + "excel-extension-guide.html"),
    "word_ext": ("Word extension", D + "word-extension-guide.html"),
    "ppt_ext": ("PowerPoint extension", D + "powerpoint-extension-guide.html"),
    "slack_ext": ("Slack extension", D + "slack-extension-guide.html"),
    "teams_ext": ("Teams extension", D + "teams-extension-user-guide.html"),
    "slack_admin": ("Slack extension access", D + "slack-extension.html"),
    # security, governance
    "custom_perm": ("Custom permissions", D + "custom-permissions.html"),
    "deny_default": ("Deny by Default", D + "custom-permissions-governance.html"),
    "approval": ("Approval workflows", D + "approval-workflows.html"),
    "smart": ("Smart Approvals", D + "smart-approvals.html"),
    "dlp": ("Data loss prevention", D + "data-loss-prevention.html"),
    "limits": ("Limit profiles", D + "limit-profiles.html"),
    "logs": ("Vended logs", D + "monitoring-cloudwatch-logs.html"),
    "sec_bp": ("Security best practices", D + "best-practices-security.html"),
    "data_prot": ("Data protection", D + "sec-data-protection.html"),
    "cmk": ("Customer managed keys", D + "customer-managed-keys.html"),
    "guardrails": ("Guardrails", D + "guardrails.html"),
})
SRC.update({
    # AWS product pages, What's New, blogs
    "faqs": ("Amazon Quick FAQs", "https://aws.amazon.com/quick/faqs/"),
    "customers": ("Amazon Quick 客户", "https://aws.amazon.com/quick/customers/"),
    "enterprise": ("Amazon Quick Enterprise", "https://aws.amazon.com/quick/enterprise/"),
    "wn_ga": ("What's New 2025-10 发布", WN + "2025/10/amazon-quick-suite-agentic-ai-powered-workspace"),
    "wn_memory": ("What's New 2025-12 记忆", WN + "2025/12/amazon-quick-suite-memory-chat-agents/"),
    "wn_research_flows": ("What's New 2025-12 Research 自动化",
                          WN + "2025/12/amazon-quick-suite-research-flows-report-automation"),
    "wn_tokyo": ("What's New 2026-03 东京", WN + "2026/03/amazon-quick-now-available-in-the-aws-tokyo-region/"),
    "wn_freeplus": ("What's New 2026-04 Free/Plus", WN + "2026/04/amazon-quick-free-plus/"),
    "wn_custom_apps": ("What's New 2026-04 Apps 预览", WN + "2026/04/custom-applications/"),
    "wn_june": ("What's New 2026-06 自主 agent", WN + "2026/06/amazon-quick/"),
    "wn_dlp": ("What's New 2026-08 Purview DLP", WN + "2026/08/amazon-quick-dlp-purview/"),
    "wn_m365": ("What's New 2026-08 M365 扩展",
                WN + "2026/08/amazon-quick-microsoft-365-extensions-generally-available"),
    "wn_apps_ga": ("What's New 2026-09 Apps GA", WN + "2026/09/amazon-quick-custom-apps-natural-language/"),
    "wn_max": ("What's New 2026-09 Max", WN + "2026/09/amazon-quick-max-5x-usage-power-users/"),
    "wn_desktop_ga": ("What's New 2026-09 桌面 GA",
                      WN + "2026/09/amazon-quick-desktop-app-generally-available-macos-windows/"),
    "wn_alwayson": ("What's New 2026-09 常驻 agent",
                    WN + "2026/09/amazon-quick-always-on-agents-sharper-feed-enterprise-controls/"),
    "wn_brand": ("What's New 2026-10 品牌模板",
                 WN + "2026/10/amazon-quick-brand-templates-on-brand-presentations-documents/"),
    "wn_smart": ("What's New 2026-10 Smart Approvals", WN + "2026/10/quick-smart-approvals-agentic-actions/"),
    "blog_kitsa": ("AWS 博客：Kitsa", ML + "kitsa-transforms-clinical-trial-site-selection-with-amazon-quick-automate/"),
    "blog_dlocal": ("AWS 博客：dLocal", ML + "how-dlocal-automated-compliance-reviews-using-amazon-quick-automate/"),
    "blog_godaddy": ("AWS 博客：GoDaddy", ML + "how-godaddy-transformed-its-analytics-with-amazon-quick/"),
    "blog_tradeshift": ("AWS 博客：Tradeshift",
                        ML + "evolving-from-legacy-bi-to-agentic-ai-at-tradeshift-with-amazon-quick/"),
    "blog_aderant": ("AWS 博客：Aderant", ML + "aderant-transforms-cloud-operations-with-amazon-quick/"),
    "blog_desktop_ga": ("AWS 博客：桌面应用 GA", ML + "amazon-quick-is-now-generally-available-on-desktop/"),
    "blog_sales": ("AWS 博客：销售场景",
                   ML + "transform-your-sales-organization-with-amazon-quick-your-new-agentic-ai-teammate/"),
    "blog_marketing": ("AWS 博客：市场营销场景",
                       ML + "amazon-quick-for-marketing-from-scattered-data-to-strategic-action/"),
    "blog_onboarding": ("AWS 博客：员工入职 agent", ML + "build-ai-powered-employee-onboarding-agents-with-amazon-quick/"),
    "blog_autonomous": ("AWS 博客：自主 agent", ML + "get-back-hours-every-day-with-autonomous-agents-in-amazon-quick/"),
    "blog_lease": ("AWS 博客：租约合规检查",
                   ML + "sweep-thousands-of-leases-for-compliance-using-amazon-quick-and-the-adjudicated-query-pattern/"),
    "blog_newrelic": ("AWS 博客：New Relic 事件分诊",
                      ML + "build-an-agentic-incident-triage-assistant-with-amazon-quick-and-new-relic/"),
})

SRC.update({
    # Amazon Quick on desktop and mobile (English user guide)
    "desktop_home": ("Amazon Quick on desktop", D + "amazon-quick-desktop.html"),
    "desktop_start": ("Getting started (desktop)", D + "getting-started-desktop.html"),
    "desktop_interface": ("Desktop interface", D + "desktop-interface.html"),
    "library_desktop": ("Library", D + "library-desktop.html"),
    "customize_desktop": ("Customize", D + "customize-desktop.html"),
    "chat_desktop": ("Working with chat (desktop)", D + "working-with-chat-desktop.html"),
    "agents_desktop": ("Agents (desktop)", D + "agents-desktop.html"),
    "connections_desktop": ("Connectors (desktop)", D + "connections-desktop.html"),
    "local_connectors": ("Local connectors", D + "local-connectors.html"),
    "coding_agents": ("Coding agents", D + "coding-agents.html"),
    "system_tools": ("System tools", D + "system-tools-desktop.html"),
    "mycontext": ("My context", D + "desktop-settings-my-context.html"),
    "desktop_sec": ("Desktop security and privacy", D + "desktop-security.html"),
    "desktop_settings": ("Desktop settings", D + "desktop-settings.html"),
    "desktop_ent": ("Desktop enterprise setup", D + "desktop-enterprise-setup.html"),
    "desktop_entra": ("Enterprise sign-in with Microsoft Entra ID", D + "desktop-enterprise-entra-id.html"),
    "desktop_mdm": ("Deploying with MDM", D + "desktop-enterprise-mdm.html"),
    "desktop_ts": ("Desktop troubleshooting", D + "desktop-troubleshooting.html"),
    "usage_desktop": ("Desktop usage limits", D + "usage-limits-desktop.html"),
    "mobile_home": ("Amazon Quick on mobile", D + "amazon-quick-mobile.html"),
    "prebuilt_flows": ("Pre-built flows", D + "pre-built-flows.html"),
    "automate_start": ("Getting started with Quick Automate", D + "getting-started-quick-automate.html"),
    "teams_admin": ("Teams extension user guide", D + "teams-extension-user-guide.html"),
    "wn_desktop_preview": ("What's New 2026-04 桌面版预览", WN + "2026/04/amazon-quick-macos-windows-preview/"),
    "wn_essentials": ("What's New 2026-10 Quick Essentials", WN + "2026/10/amazon-quick-essentials/"),
    "user_types": ("User types and subscriptions", D + "user-types.html"),
    "wn_desktop_signin": ("What's New 2026-11 桌面版沿用 Web 登录",
                          WN + "2026/11/amazon-quick-desktop-organization-sign-in/"),
    "desktop_adv_idp": ("Dedicated identity provider (advanced)", D + "desktop-enterprise-advanced-idp.html"),
    "desktop_managed": ("Managed deployment configuration", D + "desktop-enterprise-managed-deployment.html"),
    "wn_feed_mobile": ("What's New 2026-09 移动端 feed",
                       WN + "2026/09/amazon-quick-activity-feed-available-ios-android-mobile-devices/"),
})

S1, S2, S3, S4, S5 = "01  产品概览", "02  Quick 桌面版", "03  其他主要功能", "04  应用场景", "05  最佳实践"

SLIDES = []

SLIDES.append({
    "kind": "cover", "title": "Amazon Quick 介绍", "subtitle": "主要功能、应用场景与最佳实践 · 重点：Quick 桌面版",
    "meta": ["基于截至 2026 年 10 月的 AWS 英文官方文档与发布信息", "时长约 30 分钟"],
    "say": ["大家好。今天用大约三十分钟介绍 Amazon Quick，重点是 Quick 桌面版。内容基于截至 2026 年 10 月底的 AWS 英文官方文档和发布信息。"],
})

SLIDES.append({
    "kind": "cards", "section": "议程", "title": "今天的内容", "cols": 5, "title_pt": 16, "body_pt": 14.5,
    "cards": [
        {"key": "a1", "num": 1, "title": "产品概览", "bullets": ["定位与组成", "工作原理", "关键演进", "开通与套餐"]},
        {"key": "a2", "num": 2, "title": "桌面版", "bullets": ["定位与界面", "Chat 进阶与文档生成", "Activity feed", "Agents 与 routines", "Skills 与 Connectors",
                                                             "My context", "场景与客户", "安全、部署与最佳实践"]},
        {"key": "a3", "num": 3, "title": "其他主要功能", "bullets": ["Chat 与 chat agents", "Spaces 与 Quick Sight", "Research", "Flows 与 Automate",
                                                           "Apps、集成与治理"]},
        {"key": "a4", "num": 4, "title": "应用场景", "bullets": ["按部门的场景", "客户案例"]},
        {"key": "a5", "num": 5, "title": "最佳实践", "bullets": ["功能选型", "agent 与知识", "集成、安全与成本", "上手路径"]},
    ],
    "say": [
        ("a1", "内容分五部分。先用几页概览 Amazon Quick 的定位、工作原理、过去一年的变化和套餐。"),
        ("a2", "第二部分是重点，用十几页详细介绍 Quick 桌面版：它能做什么、怎么用、典型场景，以及安全、部署和最佳实践。"),
        ("a3,a4", "第三部分快速介绍其他主要功能，第四部分看按部门的场景和客户案例。"),
        ("a5", "最后是最佳实践和建议的上手路径。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S1, "title": "Amazon Quick 是什么", "cols": 3,
    "lead": "用自然语言聊天驱动的 AI 服务：自动化任务、分析数据、构建 Web 应用、做研究，背后由 AI agent 结合已连接的数据和应用完成请求。",
    "cards": [
        {"key": "sight", "tag": "分析", "title": "Quick Sight", "text": "交互式 BI：连接数据、构建 dashboards、嵌入分析，并提供生成式 BI。"},
        {"key": "research", "tag": "研究", "title": "Quick Research", "text": "结合 Web 与企业数据做深度研究，输出带引用的报告。"},
        {"key": "flows", "tag": "自动化", "title": "Quick Flows", "text": "业务用户用自然语言创建的 AI 工作流，处理日常重复任务。"},
        {"key": "automate", "tag": "自动化", "title": "Quick Automate", "text": "面向 power users 的端到端流程自动化，含 agent 决策与人工审核。"},
        {"key": "index", "tag": "知识", "title": "Quick Index", "text": "连接企业文档和数据源，让 AI 的回答有据可依。"},
        {"key": "apps", "tag": "应用", "title": "Apps in Amazon Quick", "text": "用自然语言描述需求，生成并发布交互式 Web 应用。"},
    ],
    "note": {"label": "演进", "text": "Amazon Quick 由 Amazon QuickSight 演进而来；QuickSight 现为其中的 Quick Sight，现有 API、SDK 和集成无需修改。"},
    "src": ["whatis", "history"],
    "say": [
        "进入第一部分。按官方定义，Amazon Quick 是一个用自然语言聊天驱动的 AI 服务，可以自动化任务、分析数据、构建 Web 应用和做研究，背后由 AI agent 结合已连接的数据和应用完成请求。",
        ("sight,research,flows", "它包含六个功能：Quick Sight 做 BI 分析，Quick Research 做带引用的深度研究，Quick Flows 让业务用户自己搭工作流。"),
        ("automate,index,apps", "Quick Automate 编排企业级的业务流程，Quick Index 连接企业文档和数据，Apps 用一段话生成 Web 应用。"),
        ("note", "Amazon Quick 由 QuickSight 演进而来，原有的 API、SDK 和集成都不需要修改。"),
    ],
})

SLIDES.append({
    "kind": "layers", "section": S1, "title": "工作原理：从一句话到完成任务",
    "lead": "Chat 是主入口；每次交互背后都是一个 agent，Spaces 组织上下文，Integrations 连接外部数据与应用。",
    "layers": [
        {"key": "l1", "label": "入口", "sub": "Meets you where you work",
         "chips": ["Web|浏览器访问", "Desktop|macOS / Windows", "Mobile|iOS / Android", "Extensions|Chrome、Microsoft 365、Slack、Teams"]},
        {"key": "l2", "label": "Chat", "sub": "主要交互界面",
         "chips": ["提问与分析|基于已连接数据回答", "生成内容|文档、图表、代码", "执行动作|在外部应用中操作", "启动任务|运行 flow 或研究"]},
        {"key": "l3", "label": "Agents", "sub": "处理每一次请求",
         "chips": ["Instructions|定义行为", "Knowledge|回答的依据", "Tools|对外执行动作", "默认 agent + custom agents|按领域构建"]},
        {"key": "l4", "label": "Spaces", "sub": "组织并共享上下文",
         "chips": ["Files|文档、音视频、代码", "Dashboards 与 Topics|结构化数据", "Knowledge bases|同步的企业内容", "Connectors|可用的动作"]},
        {"key": "l5", "label": "Integrations", "sub": "连接外部世界",
         "chips": ["Knowledge bases|S3、SharePoint 等", "Connectors|OpenAPI、MCP", "Extensions|嵌入日常工具", "Structured data|数据库、数仓、数据湖"]},
    ],
    "src": ["how", "whatis"],
    "say": [
        ("l1", "再看它怎么工作。入口有网页、桌面应用、手机，以及 Chrome、Microsoft 365、Slack 和 Teams 里的扩展。"),
        ("l2", "所有入口的核心都是 Chat：你提问或描述任务，Quick 判断是从数据里回答、生成内容、运行工作流、做研究，还是去外部应用执行动作。"),
        ("l3", "每次交互背后都是一个 agent，由三部分组成：指令决定行为，知识决定回答的依据，工具让它能对外执行动作。"),
        ("l4,l5", "Spaces 把文件、仪表板、知识库和连接器组织成团队共享的上下文；Integrations 负责连接外部的数据和应用。"),
    ],
})

SLIDES.append({
    "kind": "timeline", "section": S1, "title": "一年来的关键演进",
    "lead": "按 AWS What's New 发布日期与文档历史整理（2025-10 至 2026-10）。",
    "items": [
        {"key": "t1", "date": "2025-10", "title": "Quick Suite 发布", "text": "QuickSight 并入；Research、Flows、Automate 上线"},
        {"key": "t2", "date": "2025-12", "title": "Memory", "text": "chat agents 支持 memory；Research 可放进 Flows"},
        {"key": "t3", "date": "2026-03", "title": "区域扩展", "text": "Tokyo、Frankfurt、London 完整支持"},
        {"key": "t4", "date": "2026-04", "title": "桌面版预览", "text": "Free / Plus 套餐；桌面应用与 Apps 预览；聊天内生成文档"},
        {"key": "t5", "date": "2026-06", "title": "自主 agent", "text": "可设自主级别；Free / Plus 账户的 Apps 可公开发布"},
        {"key": "t6", "date": "2026-08", "title": "企业治理", "text": "Purview DLP、approval policies、per-user limits；M365 扩展 GA"},
        {"key": "t7", "date": "2026-09", "title": "桌面版 GA", "text": "always-on agents；Max 套餐；Apps GA；agent hours 上调"},
        {"key": "t8", "date": "2026-10", "title": "Smart Approvals", "text": "桌面与移动端自动审批；Brand assets；新加坡区域"},
    ],
    "src": ["wn_ga", "wn_memory", "wn_research_flows", "wn_tokyo", "wn_freeplus", "wn_desktop_preview", "wn_june",
            "wn_dlp", "wn_m365", "wn_desktop_ga", "wn_alwayson", "wn_smart", "wn_brand"],
    "say": [
        ("t1", "过去一年变化很快。2025 年 10 月，Amazon Quick Suite 发布，QuickSight 并入其中。"),
        ("t2,t3", "12 月加入 memory，Research 可以放进 Flows 定期运行；2026 年 3 月扩展到东京、法兰克福和伦敦。"),
        ("t4", "4 月是转折点：推出不需要 AWS 账户的 Free 和 Plus 套餐，桌面应用和 Apps 开始预览。"),
        ("t5,t6", "6 月，agent 可以按设定的自主级别独立工作；8 月集中补齐企业治理，Microsoft 365 扩展也正式发布。"),
        ("t7", "9 月桌面应用正式发布，定时任务和监控类 agent 在云端常驻运行，合上电脑也会继续；同时推出 Max 套餐，Professional 的 agent hours 从每月 4 小时增至 8 小时，Enterprise 从 8 小时增至 18 小时。"),
        ("t8", "10 月又推出了桌面和移动端的 Smart Approvals，以及 Brand assets 品牌模板。"),
    ],
})

SLIDES.append({
    "kind": "table", "section": S1, "title": "开通方式与套餐",
    "head": ["套餐", "开通方式", "每用户每月", "主要特点"],
    "widths": [1.35, 1.5, 2.1, 7.2], "pt": 12.5, "hpt": 13.5,
    "rows": [
        ["Free", "aws.com/quick", "$0", "1 个用户、1 GB；chat、custom chat agents、Research、Flows、Apps、桌面应用"],
        ["Plus", "aws.com/quick", "年付 $20 / 月付 $25", "最多 300 个用户、每席位 10 GB；团队共享 Spaces 与 knowledge bases；浏览器与 Microsoft 365 扩展"],
        ["Max", "aws.com/quick", "年付 $100 / 月付 $125", "用量与索引存储均为 Plus 的 5 倍，面向重度用户"],
        ["Essentials", "AWS 控制台", "$3", "2026-10-30 新增的入门套餐：chat、Research、Flows、Apps、桌面应用，查看 Quick Sight dashboards；每用户 1 GB、每月 1 agent hour*"],
        ["Professional", "AWS 控制台", "$20", "Essentials 的全部能力；每用户 25 GB 池化索引、每月 8 agent hours"],
        ["Enterprise", "AWS 控制台", "$40", "每用户 50 GB、每月 18 agent hours；Quick Automate，创建 dashboards 与 datasets，审批与认证已发布资产"],
    ],
    "note": {"label": "注意", "text": "Essentials、Professional、Enterprise 每账户另收 $250/月基础设施费；超额 $3 / agent hour，Essentials 与 Professional 须先由管理员设 limit profile。* 2027-01-31 前为 3 小时。Quick Sight 分析、Quick Automate 与 API 仅限控制台开通的账户；首次开通可免费试用 30 天、最多 25 个用户。", "h": 0.85},
    "src": ["pricing", "plans", "signup", "wn_essentials", "user_types", "wn_max", "wn_alwayson"],
    "say": [
        "开通方式有两种：个人和小团队在 aws.com/quick 注册，不需要 AWS 账户；企业通过 AWS 管理控制台开通，接入 IAM Identity Center 等企业身份。",
        ("r1,r2,r3", "注册方式有 Free、Plus、Max 三档：Free 免费、一个用户；Plus 按年付每用户每月 20 美元，可以团队共享；Max 每用户每月 100 美元，用量是 Plus 的 5 倍。"),
        ("r4", "控制台开通有三种订阅。10 月 30 日新增的 Essentials 是面向全员的入门套餐，每用户每月 3 美元，包含 chat、Research、Flows、Apps 和桌面应用，还能查看 Quick Sight 仪表板；每月含 1 个 agent hour，2027 年 1 月底之前为 3 个。原来按用户计费的 Quick Sight Reader 会升级为 Essentials，不增加每用户费用，各区域分阶段推出。"),
        ("r5,r6", "Professional 和 Enterprise 每用户每月 20 和 40 美元，每月分别含 8 个和 18 个 agent hours；只有 Enterprise 可以用 Quick Automate 和创建仪表板。这三种订阅，每个账户另收每月 250 美元的基础设施费。"),
        ("note", "用量按 agent hours 按秒计量，超出配额按每 agent hour 3 美元计费；Essentials 和 Professional 需要管理员先设置 limit profile，只能在限额内超额。另外，Quick Sight 的仪表板与分析、Quick Automate 和 API，只在控制台开通的账户里提供。"),
    ],
})

# ----------------------------------------------------------------------------- 02 Quick 桌面版
SLIDES.append({
    "kind": "cards", "section": S2, "title": "Quick 桌面版：会主动干活的 AI 同事", "cols": 3,
    "lead": "官方定位 “an agentic AI teammate”：连接本地文件和日常工具，接受委派、独立跟进并交回结果。2026-09-09 正式发布。",
    "cards": [
        {"key": "c1", "title": "云端：Quick 本体", "text": "会话、memory、knowledge graph、agent 产出和索引存于 Amazon Quick 账号，Web、桌面、移动共用；routines 在云端运行，合上电脑也继续。"},
        {"key": "c2", "title": "本机：桌面版新增", "text": "授权文件夹中的文件、在自己浏览器里的 Browser Automation、本地代码执行、local MCP server 与 coding agents。"},
        {"key": "c3", "title": "平台要求", "text": "macOS 12+（Apple Silicon）；Windows 10+（x64）；8 GB 内存；安装需 2 GB，索引与 knowledge graph 建议 10 GB 以上。"},
        {"key": "c4", "title": "登录", "text": "个人账号用 email、Amazon、Apple、Google 或 GitHub；企业账号输入 Quick account name，在浏览器沿用 Web 端登录方式，需管理员先开通 desktop access。"},
        {"key": "c5", "title": "可用 Region（GA 时）", "text": "us-east-1、us-west-2、eu-west-1、eu-west-2、eu-central-1、ap-northeast-1、ap-southeast-2。"},
        {"key": "c6", "title": "Mobile companion", "text": "iOS / Android：chat、Activity feed、dashboards、审批 agent 请求；会话与上下文跨设备同步。"},
    ],
    "src": ["desktop_home", "desktop", "desktop_start", "desktop_ent", "wn_desktop_ga", "wn_desktop_signin", "mobile_home"],
    "say": [
        "进入第二部分，也是今天的重点：Quick 桌面版。官方对它的定位是 an agentic AI teammate，一个会主动干活的 AI 同事：它连接你的本地文件和日常工具，你把任务委派给它，它独立跟进，再把结果交回来。桌面版在 2026 年 9 月 9 日正式发布。",
        ("c1", "先理解架构。Quick 本体运行在云端：会话、记忆、知识图谱、agent 的产出和索引，都保存在你的 Amazon Quick 账号里，网页、桌面和手机共用。所以定时任务在云端运行，合上电脑也会继续。"),
        ("c2", "桌面版增加的是对本机的访问：你授权的文件夹、在你自己浏览器里的自动化操作、本地代码执行，以及本地的 MCP server 和 coding agent。"),
        ("c3,c4", "它支持 Apple Silicon 的 macOS 12 以上和 64 位 Windows 10 以上，内存 8 GB。个人账号可以用邮箱或社交账号登录；企业账号输入 Quick 的 account name，在浏览器里沿用网页版的登录方式，前提是管理员已经开通桌面访问。"),
        ("c5,c6", "正式发布时在 7 个区域提供。另外还有 iOS 和 Android 的移动端，用来聊天、看 feed、看仪表板和审批 agent 的请求，会话在各设备之间同步。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "界面与导航", "cols": 3,
    "lead": "左侧 navigation rail、主内容区、top bar 和 overlay panels；Home 页的 chat composer 是主入口。",
    "cards": [
        {"key": "c1", "title": "Home", "text": "按时段问候、chat composer、未连接数据源的设置卡片，以及 Quick Briefs（最高优先级 feed 条目的摘要）。"},
        {"key": "c2", "title": "Composer", "text": "选择 agent、response mode（Fast / Balanced / Smart）和 thinking effort（Off / Low / Medium / High），可开 Incognito chat。"},
        {"key": "c3", "title": "Navigation rail", "text": "Chat、Feed、Library、Customize、Apps、Spaces，以及 More 中的 Research、Data、Dashboards、Automations 等。"},
        {"key": "c4", "title": "Library", "text": "集中存放文档、演示、表格、图片、音视频，以及 apps、spaces、agents、skills、research、dashboards、flows 等资产。"},
        {"key": "c5", "title": "Customize", "text": "五个 tab：Agents、Skills、Connectors、Knowledge、Brand assets；Add to Quick 目录可安装共享条目和 Amazon 官方 skills。"},
        {"key": "c6", "title": "Top bar 与 panels", "text": "Mission Control 入口与连接状态；Session tabs、All data and apps、session activity 等 overlay panels。"},
    ],
    "src": ["desktop_interface", "library_desktop", "customize_desktop"],
    "say": [
        "看一下界面。桌面版由左侧导航栏、主内容区、顶栏和浮层面板组成。",
        ("c1,c2", "首页的聊天输入框是主入口，首页还会显示 Quick Briefs，也就是最高优先级 feed 条目的摘要。输入框里可以选择 agent、回答模式和思考强度：Fast 延迟最低，Balanced 适合大多数任务，Smart 推理最充分；需要隐私时可以开 Incognito。"),
        ("c3,c4", "导航栏有 Chat、Feed、Library、Customize、Apps、Spaces，以及 Research、Dashboards、Automations 等更多入口。Library 集中存放生成的文档，以及 agent、skill、研究报告和仪表板等资产。"),
        ("c5,c6", "Customize 是配置中心，分 Agents、Skills、Connectors、Knowledge 和 Brand assets 五个标签。顶栏固定有 Mission Control 的入口和连接状态。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "Chat 进阶：从对话到交付", "cols": 3,
    "lead": "桌面版 Chat 面向复杂多步骤任务：Plan mode 先计划，任务可送到后台，/goal 持续推进直到完成。",
    "cards": [
        {"key": "c1", "title": "Add context", "text": "+ 菜单：Upload files（单个 50 MB）、Local folders、Web search、Spaces；附加 space 后默认只用其内容回答，可要求扩大范围。"},
        {"key": "c2", "title": "Slash commands 与 /goal", "text": "/clear、/compact、/export、/mode、/skills、/connectors 等；/goal 让 agent 持续工作并自行复核，完成后才交回。"},
        {"key": "c3", "title": "Plan mode 与 Deep research", "text": "Plan mode 先拆成结构化步骤，审阅修改后再执行；Deep research 做多来源调研，显示实时进度。"},
        {"key": "c4", "title": "后台运行与 branches", "text": "Ctrl+B / Cmd+B 把任务送到后台，完成后通知；每次编辑或重试保留为分支，可切换比较。"},
        {"key": "c5", "title": "Incognito mode", "text": "不读写长期 memory 和 knowledge graph，不进 Recents，离开即删除；必须在发出第一条消息前开启。"},
        {"key": "c6", "title": "Citations 与 sources", "text": "inline citations 和 Sources 面板，来源含网页、文件、已连接数据和 memories；可 boost 或移除某条 memory。"},
    ],
    "src": ["chat_desktop"],
    "say": [
        "桌面版的 Chat 为复杂的多步骤任务提供了专门的功能。",
        ("c1", "通过加号菜单可以给对话加上下文：上传文件、授权的本地文件夹、网页搜索或者 Spaces。附加 space 之后，Quick 默认只用这个 space 的内容回答，不会自行越界，适合保密和合规场景；需要时也可以让它扩大搜索范围。"),
        ("c2", "斜杠命令里最值得一提的是 /goal：你把一个目标交给 agent，它会持续工作、自己复核，完成后才交回，而普通对话答一次就停下来等你。"),
        ("c3,c4", "复杂任务可以先用 Plan mode 拆成结构化步骤，你审阅修改后再执行；Deep research 做多来源调研并显示实时进度。按 Command 加 B 可以把任务送到后台，完成后通知你；每次编辑或重试都保留为一个分支，方便比较。"),
        ("c5,c6", "Incognito 模式不读写长期记忆和知识图谱，也不进历史记录，但必须在发出第一条消息之前开启。回答带行内引用，来源列表里还会列出用到的记忆，你可以加强或移除。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "生成文档与 Brand assets", "cols": 3, "body_pt": 14,
    "lead": "在对话中生成 .pptx、.docx、.xlsx、PDF、Markdown、HTML 和交互式可视化；Web 版同样支持文档生成。",
    "cards": [
        {"key": "c1", "title": "Session tabs", "text": "生成的 artifact 在会话旁以 tab 打开，可查看编辑；selection mode 把选中的文字、图片、表格作为下一轮上下文。"},
        {"key": "c2", "title": "保存与分享", "text": "artifact 可存到本地或 Library，也可下载、分享或在 chat 中继续修改。"},
        {"key": "c3", "title": "Image Generation", "text": "基于 Amazon Nova Canvas 按文字生成和编辑图片，含去背景、变体和 outpaint。"},
        {"key": "c4", "title": "Brand assets", "text": "brand manager 上传 .pptx / .potx / .docx / .dotx 模板或经 connector 拉取，Quick 抽取颜色、文字样式、logo、结构和 Rules。"},
        {"key": "c5", "title": "审核与发布", "text": "人工审核 When to use、Rules、Logo 后发布到全组织；仅 Enterprise edition（控制台开通的账户）。"},
        {"key": "c6", "title": "用户侧体验", "text": "生成时 Visual Style 预选最匹配的组织模板；请求违反模板规则时，Quick 解释原因并给出合规替代方案。"},
    ],
    "note": {"label": "官方建议", "text": "写清内容、结构和格式；尽量上传 CSV、Excel 或 JSON 源数据，避免示例占位数字；先出初稿再逐步修改。"},
    "src": ["chat_desktop", "docgen", "system_tools", "brand", "wn_brand"],
    "say": [
        "Quick 能直接产出交付物：在对话里就可以生成 PPT、Word、Excel、PDF、Markdown、HTML 和交互式可视化，网页版也支持文档生成。",
        ("c1,c2", "在桌面版里，生成的文件会在会话旁边以标签页打开，可以直接查看和编辑；选中其中的文字、图片或表格，就能作为下一轮的上下文继续修改。文件可以存到本地或 Library，也可以下载、分享，或者回到对话里继续修改。"),
        ("c3", "图片生成基于 Amazon Nova Canvas，可以按文字生成和编辑图片，包括去背景、生成变体和扩图。"),
        ("c4,c5", "企业最关心品牌一致。10 月推出的 Brand assets 让品牌管理员上传 PPT 或 Word 模板，Quick 会抽取颜色、文字样式、logo、版式结构和使用规则，人工审核后发布到全组织。这项功能只在 Enterprise edition 提供。"),
        ("c6", "员工生成文档时，Quick 会预选最匹配的组织模板；如果请求违反了模板规则，它会解释原因，并给出合规的替代方案。"),
        ("note", "官方建议：把内容、结构和格式写清楚，尽量上传源数据，先出初稿再逐步修改。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "Activity feed：每天的工作入口", "cols": 3,
    "lead": "Feed agent 读取已连接的消息、邮件和日历，用 knowledge graph 判断重要性并给出建议动作；使用 feed 本身不消耗 agent hours。",
    "cards": [
        {"key": "c1", "title": "Feed", "text": "按 Important / Informational / Low priority 排序；条目含来源、AI 摘要和建议动作，回复类附草稿；相关条目合并为线程。"},
        {"key": "c2", "title": "Briefing", "text": "每日置顶卡片：隔夜动态、当日日程、待决事项与到期跟进；每天上午、中午、下午刷新三次。"},
        {"key": "c3", "title": "Calendar", "text": "今明两天的时间网格和 Quick Suggests：空闲时段一键 block focus time，或带预填 prompt 开始会前准备。"},
        {"key": "c4", "title": "To-dos", "text": "个人任务列表，含截止日期和重要性，可由 feed 条目直接生成。"},
        {"key": "c5", "title": "Auto resolve 与 Catch-up", "text": "已回复、已过期或被取代的条目自动清除；离开后回来，按重要性汇总各服务动态。"},
        {"key": "c6", "title": "Always on", "text": "在云端运行：应用关闭或电脑关机时 feed 仍在更新；scheduled tasks 和 monitoring agents 把结果发到 feed。"},
    ],
    "src": ["feed", "wn_alwayson"],
    "say": [
        "Activity feed 是桌面版每天的工作入口。Feed agent 读取你已连接的消息、邮件和日历，比如 Slack 和 Outlook，用知识图谱判断哪些对你重要，并给出建议动作。使用 feed 本身不消耗 agent hours。",
        ("c1", "条目按重要、一般和低优先级三级排序，每条有来源、AI 摘要和建议动作，需要回复的会附上草稿，相关条目合并成一个线程。"),
        ("c2", "顶部是每日简报，汇总隔夜动态、当天日程、待决事项和到期的跟进，每天上午、中午、下午各刷新一次。"),
        ("c3,c4", "Calendar 标签页可以在空闲时段一键预留专注时间，或者带着预填的提示词开始会前准备；To-dos 可以把 feed 条目直接变成待办。"),
        ("c5,c6", "处理过的条目会自动清除，离开一段时间回来，Catch-up 会按重要性汇总动态。因为 feed 在云端运行，应用关闭甚至电脑关机时它也在更新，定时任务和监控 agent 的结果也会发到这里。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "Agents、routines 与 Mission Control", "cols": 3,
    "lead": "Custom agent 有自己的 instructions、knowledge 和 tools，只能访问用户本人有权访问的资源，并可以按计划在云端运行。",
    "cards": [
        {"key": "c1", "title": "创建 agent", "text": "Customize > Agents > Create：From chat 或 From file；Instructions 最长 50,000 字符，可设 welcome message 和 starter prompts。"},
        {"key": "c2", "title": "Capabilities 与发布", "text": "Web search、Skills、Spaces、Connections；先改 draft，写 release notes 再 publish，发布后才能分享。"},
        {"key": "c3", "title": "Routines", "text": "目前为 schedule 类型：频率与时区、可用的 MCP servers 与 tools、Instructions、Model 与 Thinking effort；也可在 chat 中用自然语言创建。"},
        {"key": "c4", "title": "云端运行", "text": "routine 在云端运行，合上电脑也继续；需要本机文件、Browser Automation 或本地代码的步骤，要求当时电脑开机、应用在线。"},
        {"key": "c5", "title": "Mission Control", "text": "集中查看所有 agent 运行、处理 Needs input 请求、管理 routines；KPI：Failed runs、Active now、Routines completed、Runs this week。"},
        {"key": "c6", "title": "Creator analytics", "text": "按 Agents / Apps 统计已发布资产的使用情况，每小时刷新；Activity 页显示 agent hours 用量。"},
    ],
    "src": ["agents_desktop", "mission", "wn_alwayson"],
    "say": [
        "接下来是 agent。在桌面版里，你可以创建自己的 agent，它有自己的指令、知识和工具，并且只能访问你本人有权访问的资源。",
        ("c1,c2", "可以在对话里描述需求，由 Quick 生成名称、描述和指令草稿，也可以从文件导入已有的 agent 定义；能力上可以开启网页搜索，指定 Skills、Spaces 和连接。修改先存为草稿，写好发布说明再发布，发布后才能分享。"),
        ("c3,c4", "让 agent 真正替你干活的是 routine。目前 routine 按计划触发：设定频率和时区，指定它能用的 MCP server 和工具，写好指令，选择模型和思考强度。也可以直接在对话里说，比如每天早上九点检查我的频道，总结我错过的内容。routine 在云端运行；只有读本机文件、浏览器自动化或本地代码执行的步骤，需要当时电脑开机、桌面应用在线，否则这些步骤会暂时不可用。"),
        ("c5,c6", "所有 agent 的运行情况集中在 Mission Control：看正在运行的任务、处理需要你输入的请求、管理 routine，还有失败次数、本周运行次数等指标；Creator analytics 统计你发布的 agent 和应用被使用的情况。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "Skills：把做事方法沉淀下来", "cols": 2,
    "lead": "Skill 是可复用的任务指令：一个根目录含 SKILL.md 的文件夹，可以引用 tools，并打包脚本、模板和示例。",
    "cards": [
        {"key": "c1", "title": "工作方式", "text": "两阶段加载：Discovery 按名称和描述检索，Activation 时读入完整指令；可点名使用，也会自动激活（如做演示时加载 Presentations skill）。"},
        {"key": "c2", "title": "创建", "text": "From chat、From file（.md / .zip）、From folder；多步任务完成后，Quick 可能提议把这次的做法保存为 skill。"},
        {"key": "c3", "title": "版本与分享", "text": "Draft 与 Published 分离；Publishing 不等于 Sharing，可分享给个人、组或 Share with all；Viewer 自动跟随 owner 的发布版。"},
        {"key": "c4", "title": "官方目录与治理", "text": "Add to Quick 中有 Amazon 官方 skills（通用生产力、Sales、Marketing、Legal、Finance 等）；管理员可限制分享或要求分享审批。"},
    ],
    "note": {"label": "示例", "text": "按品牌规范写博客、按模板准备每周状态更新；System skills 覆盖文档、演示、表格、web browsing、code execution 和 transcription。"},
    "src": ["skills"],
    "say": [
        "Skills 用来把做事的方法沉淀下来。一个 skill 就是一个根目录里有 SKILL.md 的文件夹，写明描述和步骤，可以引用工具，还可以打包脚本、模板和示例。",
        ("c1", "它分两阶段加载：平时只按名称和描述检索，真正用到时才读入完整指令。你可以点名使用，它也会自动激活，比如做演示时自动加载演示相关的 skill。"),
        ("c2", "创建方式有三种：从对话、从文件或从文件夹。一个多步任务做完之后，Quick 还可能主动提议，把这次的做法保存成 skill。"),
        ("c3,c4", "Skill 有草稿和发布两个版本，发布不等于分享，可以分享给个人、组或者全员，被分享者自动跟随最新的发布版。Add to Quick 目录里还有 Amazon 官方提供的 skills，覆盖通用生产力，销售、市场、法务等团队角色，以及金融、医疗与生命科学、能源与公用事业等行业；管理员可以限制分享，或者要求审批。"),
        ("note", "官方的例子包括按品牌规范写博客、按模板准备每周状态更新。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "Connectors：云服务、本地 MCP 与 coding agents", "cols": 2, "body_pt": 13.5,
    "lead": "Customize > Connectors 分四类：Cloud connectors、System tools、Local connectors 和 Coding agents。",
    "cards": [
        {"key": "c1", "title": "Cloud connectors", "text": "Outlook、SharePoint、OneDrive、Slack、Jira、Asana、Salesforce 与远程 MCP，所有设备可用；默认 Amazon-hosted OAuth，企业可换自有 OAuth 应用。"},
        {"key": "c2", "title": "System tools", "text": "Web Search、File operations、Browser Automation、Image Generation、Transcription、Code Execution、Explainability 等；默认 Always Allow，可按读写分别调整。"},
        {"key": "c3", "title": "Local connectors（local MCP）", "text": "Local（运行 python、npx、node、uvx）、Import（读取 Kiro、Claude Code 等的配置，如 ~/.kiro/settings/mcp.json）、Remote（URL + token）；仅本机开机联网时可用。"},
        {"key": "c4", "title": "Coding agents", "text": "通过 Agent Client Protocol (ACP) 接入 Kiro、Claude Code 等；preset 可设每个工具的权限、可写路径和模型。"},
    ],
    "note": {"label": "工具权限", "text": "Owner 级 Let Users Choose / Always Ask / Disable；用户级默认写操作 Ask Each Time、读操作 Always Allow；MCP sync 新发现的工具默认禁用，待 owner 审核。", "h": 0.8},
    "src": ["connections_desktop", "local_connectors", "coding_agents", "system_tools", "tool_perm"],
    "say": [
        "桌面版的连接分四类。",
        ("c1", "第一类是云端连接器，比如 Outlook、SharePoint、Slack、Jira、Salesforce 和远程 MCP，在所有设备上都能用，默认通过 Amazon 托管的 OAuth 登录，企业也可以换成自己的 OAuth 应用。"),
        ("c2", "第二类是系统工具，包括网页搜索、文件操作、浏览器自动化、图片生成、语音转写和代码执行等，默认全部允许，可以按读写分别收紧。"),
        ("c3", "第三类是本地 MCP server：可以直接运行 python、npx 这类命令，可以导入 Kiro、Claude Code 已有的 MCP 配置文件，也可以填写远程地址。本地连接只在这台电脑开机联网时可用。"),
        ("c4", "第四类是 coding agent，通过 Agent Client Protocol 接入 Kiro、Claude Code 等工具，比如让 Kiro 重构一个模块，让 Claude Code 给函数补测试；用官方 preset 添加的 agent，还能按工具设权限、限定可写路径。"),
        ("note", "权限方面，连接器所有者可以设为让用户选择、始终询问（对所有用户强制）或禁用；用户这边默认写操作每次询问、读操作直接允许；新同步到的 MCP 工具默认禁用，要所有者审核后才开放。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "本地知识与 My context", "cols": 2,
    "lead": "Quick 越用越懂你：本地文件夹可以索引，Memories 记住偏好与做法，Knowledge graph 梳理人和事的关系。",
    "cards": [
        {"key": "c1", "title": "Knowledge（本地文件夹）", "text": "添加文件夹只授予访问，索引默认关闭；每个文件夹可分别开启全文索引和 knowledge graph 抽取，并显示预计月度用量占预算的比例。"},
        {"key": "c2", "title": "索引控制", "text": "可设 Max file age、扩展名、Exclude patterns；Rebuild index 前先给出成本估算；文件夹权限分 Full Access / Read Only / Ask Each Time。"},
        {"key": "c3", "title": "Memories", "text": "从对话中学习 facts、preferences、procedures、patterns；默认助手和每个 custom agent 各有一份；可 Boost、Forget、Edit，并标明 Told 或 Learned。"},
        {"key": "c4", "title": "Knowledge graph", "text": "从已连接服务和开启抽取的文件夹中建立人员、项目、组织、事件等实体及关系，跨 agent 共享；可在 chat 中 @ 图谱里的人。"},
    ],
    "src": ["knowledge_desktop", "mycontext", "memories", "kg", "chat_desktop"],
    "say": [
        "桌面版的一个特点是越用越懂你，靠的是三样东西。",
        ("c1,c2", "第一是本地知识。添加一个文件夹只是授予访问，索引默认关闭；你可以按文件夹分别开启全文索引和知识图谱抽取，界面会显示预计占用多少月度预算。还可以按文件年龄、扩展名和排除规则控制范围，重建索引之前会先给出成本估算。"),
        ("c3", "第二是记忆。Quick 从对话里学习事实、偏好、流程和习惯，默认助手和每个自定义 agent 各有一份记忆，每条都标明是你告诉它的还是它学到的，你可以加强、遗忘或者修改。"),
        ("c4", "第三是知识图谱。它从已连接的服务和文件夹里梳理出人员、项目、组织和事件之间的关系，在所有 agent 之间共享，对话中还可以直接 @ 图谱里的人。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "桌面版典型场景", "cols": 3,
    "lead": "以下场景来自官方文档、What's New 和 AWS 博客。",
    "cards": [
        {"key": "c1", "title": "Morning brief", "text": "每天早上汇总未读消息、新邮件和当日日程，结果发到 Activity feed；可以在 chat 中用一句话创建。"},
        {"key": "c2", "title": "Inbox triage", "text": "每 30 分钟扫描新邮件，标出紧急事项。"},
        {"key": "c3", "title": "Project / Competitive monitor", "text": "每天汇总某个频道的项目进展；每周搜索指定公司的新闻并生成报告。"},
        {"key": "c4", "title": "Meeting prep", "text": "每次会议前收集相关上下文生成简报，结果发到 Activity feed 或已连接的应用。"},
        {"key": "c5", "title": "开发协作", "text": "local MCP 连接数据库、内部 API 和开发工具；让 Kiro 重构模块，让 Claude Code 为函数写测试。"},
        {"key": "c6", "title": "转写与整理", "text": "会议录音、语音备忘、访谈音频先 Transcription，再做摘要和问答。"},
    ],
    "note": {"label": "一天的工作", "text": "在笔记本上一句话委派客户会议准备，Quick 后台整理简报；早上在手机上处理 feed、批准简报的补充内容；回到电脑在 Mission Control 查看成果并分享给团队（AWS 博客示例）。", "h": 0.8},
    "src": ["mission", "wn_feed_mobile", "desktop", "coding_agents", "system_tools", "blog_desktop_ga"],
    "say": [
        "来看桌面版的典型场景，都来自官方文档和博客。",
        ("c1,c2", "先看定时 routine。比如晨间简报：每天早上汇总未读消息、新邮件和当天日程，官方例子是每天七点半告诉我今天有哪些客户会议，并给出三条准备要点。再比如收件箱分拣，每三十分钟扫描一次新邮件，标出紧急事项。"),
        ("c3,c4", "还有项目和竞争监控：每天汇总某个频道的项目进展，每周搜索指定公司的新闻出报告；以及会前准备，每次会议前收集相关上下文生成简报；这些 routine 的结果发到 Activity feed 或已连接的应用。"),
        ("c5,c6", "对技术团队，可以用本地 MCP 连接数据库和内部 API，把开发任务交给 Kiro 或 Claude Code；对所有人，会议录音、语音备忘和访谈音频都可以先转写，再做摘要和问答。"),
        ("note", "AWS 博客描述了这样一天：一家制造企业的客户经理在笔记本上用一句话委派客户会议准备，Quick 在后台整理简报；早上在手机上处理 feed、批准简报的补充内容；回到电脑后在 Mission Control 查看完成的工作，分享给负责该客户的团队；会后再在手机上让 Quick 发出客户跟进。"),
    ],
})

SLIDES.append({
    "kind": "quotes", "section": S2, "title": "客户声音：Quick 桌面版", "cols": 3,
    "lead": "引述来自 AWS 桌面版 GA 博客（2026-09-10），中文为要点转述。",
    "quotes": [
        {"company": "Southwest Airlines", "who": "Justin Bundick · VP Technology Intelligence Platforms",
         "quote": "团队用自然语言提出复杂问题，几秒内得到有依据、可信的答案，不必再等临时报表；已用于市场分析等场景。", "use": "AI 计划覆盖 70,000+ 员工的运营"},
        {"company": "Labcorp", "who": "Chuck Metturdharma · VP & Chief AI Officer",
         "quote": "上手容易；knowledge graph 和 memory 适应个人的工作方式；可以创建异步代办的 agent，从概念到可用原型的时间大幅缩短。", "use": "GA 前评估"},
        {"company": "PGA TOUR", "who": "Randall Kato · VP Golf Technology",
         "quote": "业务专家自己完成原本排在技术积压里的工作，原型从数周缩短到数天；有了移动端，想法一出现就能行动。", "use": "桌面 + 移动端"},
    ],
    "src": ["blog_desktop_ga"],
    "say": [
        "再看客户怎么评价桌面版，引述来自 AWS 的正式发布博客。",
        ("q1", "西南航空表示，团队可以用自然语言提出复杂问题，几秒钟内得到有依据、可信的答案，不必再等临时报表，目前已经用于市场分析等场景。"),
        ("q2", "Labcorp 的首席 AI 官认为上手很容易，知识图谱和记忆会适应个人的工作方式，还可以创建异步替你干活的 agent，从概念到可用原型的时间大幅缩短。"),
        ("q3", "PGA TOUR 说，业务专家可以自己完成原本排在技术积压里的工作，原型从几周缩短到几天；有了移动端，想法一出现就能马上行动。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "桌面版的安全、隐私与审批", "cols": 3,
    "lead": "AWS 不使用会话、文件或个人上下文训练或改进 AI 模型。",
    "cards": [
        {"key": "c1", "title": "数据存放", "text": "会话、memory、knowledge graph、Library 和索引在云端按用户隔离；本机只存应用配置、文件夹授权和本地 MCP / coding agent 配置，登录凭据在操作系统凭据库。"},
        {"key": "c2", "title": "文件访问", "text": "操作系统级 sandbox，只访问显式授权的文件夹，可随时撤销；系统临时目录始终可访问。"},
        {"key": "c3", "title": "三级权限模型", "text": "System tools：Always Allow / Ask Each Time / Always Deny；connectors 另有 owner 级设置；scheduled agents 同样受约束；单次审批 12 小时有效。"},
        {"key": "c4", "title": "Smart Approvals", "text": "仅 desktop 与 mobile app：低风险、符合请求的动作自动批准；对外发送、改权限、删除、付款等转人工；审批记入 CloudTrail。"},
        {"key": "c5", "title": "管理员控制", "text": "Custom permissions 中的 Quick desktop 能力组可逐项关闭，如 Automate browser actions、Execute code locally、Use coding agents (ACP)。"},
        {"key": "c6", "title": "浏览器注意事项", "text": "Use my existing browser 需开启 remote debugging，本机应用可访问已登录的会话；不用时应关闭。"},
    ],
    "src": ["desktop_sec", "smart", "custom_perm", "usage_desktop", "desktop_settings"],
    "say": [
        "桌面版能访问本机，安全设计就格外重要。首先，AWS 明确不使用你的会话、文件或个人上下文训练或改进模型。",
        ("c1,c2", "数据方面，会话、记忆、知识图谱和索引在云端按用户隔离，本机只保存应用配置、文件夹授权和本地 MCP 与 coding agent 的配置，登录凭据放在操作系统的凭据库里。文件访问由操作系统级沙箱控制，只能访问你明确授权的文件夹，随时可以撤销。"),
        ("c3,c4", "系统工具、第三方连接器和本地工具共用一套三级权限：直接允许、每次询问、拒绝，连接器在这之上还有所有者级设置；定时运行的 agent 也受同样约束。Smart Approvals 目前只在桌面和移动端提供：低风险、符合你请求的动作自动批准，对外发送、修改权限、删除、付款这类动作仍交给你确认，审批记录写入 CloudTrail。"),
        ("c5,c6", "管理员可以在 custom permissions 里逐项关闭桌面版的能力，比如浏览器自动化、本地执行代码和 coding agent。如果开启使用自己现有浏览器的选项，需要打开浏览器的远程调试，本机应用就能访问已登录的会话，不用时应该关闭。"),
    ],
})

SLIDES.append({
    "kind": "flow", "section": S2, "title": "企业部署桌面版",
    "lead": "2026-11-01 起默认沿用 Web 端已有的登录方式，管理员添加一次 desktop connector 即可开通桌面访问。",
    "body_pt": 13.5,
    "steps": [
        {"key": "s1", "title": "开通桌面访问", "bullets": ["Inbound connectors > Quick Desktop > Add desktop connector", "沿用现有登录方式，无需在 IdP 注册应用", "立即对全账户生效，可用 custom permissions 分批上线"]},
        {"key": "s2", "title": "专用 IdP", "bullets": ["可选：Configure Identity Provider，注册 public OIDC client", "指南：Microsoft Entra ID、Google Workspace、Okta、Ping Identity", "IdP 邮箱须与 Quick 用户邮箱完全一致"]},
        {"key": "s3", "title": "MDM 分发", "bullets": ["per-machine 安装包：macOS .pkg、Windows Admin Setup", "Intune、Jamf、Kandji、Workspace ONE", "企业 CA 用证书 profile 下发"]},
        {"key": "s4", "title": "策略与网络", "bullets": ["DisableSocialLogin 禁用社交账号登录", "DisableAutoUpdates 控制版本节奏", "沿用系统代理；放行 Quick 出站域名"]},
    ],
    "note": {"label": "官方建议", "text": "保留 patch 级自动更新；用专用 IdP 时授予 offline_access。已有 desktop extension 可继续使用，迁移到 desktop connector 前先把应用升级到 1.1.4053 以上。", "h": 0.8},
    "src": ["desktop_ent", "wn_desktop_signin", "desktop_adv_idp", "desktop_entra", "desktop_mdm", "desktop_managed", "desktop_sec"],
    "say": [
        "企业怎么部署桌面版？11 月 1 日起流程简化了：桌面版默认沿用网页版已有的登录方式。整体分四步。",
        ("s1", "第一步开通桌面访问：管理员在 Quick 控制台的 Inbound connectors 里添加一次 desktop connector，默认沿用 Web 端已有的登录方式，不用在 IdP 里注册应用，IAM Identity Center、IAM federation 和 Quick 托管用户都适用。添加后对全账户立即生效，想分批上线，就先用 custom permissions 限制桌面版能力。"),
        ("s2", "第二步是可选的：如果要在 IdP 里单独管理桌面登录，就选 Configure Identity Provider，注册一个公共 OIDC 客户端。官方有 Microsoft Entra ID、Google Workspace、Okta 和 Ping Identity 的指南，IdP 邮箱必须和 Quick 用户邮箱完全一致。"),
        ("s3", "第三步用 MDM 分发。官方提供按机器安装的安装包，支持 Intune、Jamf、Kandji 等工具，企业根证书用证书配置文件下发。"),
        ("s4", "第四步下发策略：用 DisableSocialLogin 禁用社交账号登录，用 DisableAutoUpdates 控制版本节奏；网络上沿用系统代理，放行 Quick 的出站域名即可。"),
        ("note", "官方建议保留补丁级的自动更新；如果用专用 IdP，记得授予 offline_access，避免用户频繁重新登录。已经用 desktop extension 的企业可以继续用，迁移前先把所有设备升级到 1.1.4053 以上。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S2, "title": "桌面版最佳实践", "cols": 3,
    "lead": "依据桌面版各功能页、故障排查和 Smart Approvals 文档整理。",
    "cards": [
        {"key": "c1", "title": "最小权限", "text": "System tools 默认全部 Always Allow：按需把写操作改为 Ask Each Time，关闭不需要的工具；只添加组织批准的 coding agents。"},
        {"key": "c2", "title": "强制人工确认", "text": "必须人工审批的动作在 connector 上设为 Always Ask，不依赖 Smart Approvals 的自动审核。"},
        {"key": "c3", "title": "控制索引成本", "text": "只索引需要的文件夹，用 Exclude patterns、Max file age 和扩展名过滤；Rebuild index 前先看成本估算。"},
        {"key": "c4", "title": "节省 agent hours", "text": "减少不必要的后台 schedule；简单任务用 Fast 模式并关闭 thinking effort。"},
        {"key": "c5", "title": "用好隐私控制", "text": "敏感对话在第一条消息前开启 Incognito；memory 有误就 Edit，Forget 时选择原因，避免重复学到。"},
        {"key": "c6", "title": "可靠的 routines", "text": "依赖本机工具的 routine，要保证运行时段电脑开机、应用在线；分享 agent 时一并分享它依赖的数据源。"},
    ],
    "src": ["system_tools", "connections_desktop", "smart", "knowledge_desktop", "desktop_ts", "chat_desktop", "memories",
            "mission", "agents_desktop"],
    "say": [
        "最后是根据官方文档整理的桌面版最佳实践。",
        ("c1,c2", "第一是最小权限。系统工具默认全部允许，建议把写操作改为每次询问，关掉不需要的工具，只接入组织批准的 coding agent；必须人工审批的动作，要由连接器所有者设为始终询问，也就是 Always Ask，而不是依赖 Smart Approvals 的自动审核。"),
        ("c3,c4", "第二是控制成本。只索引真正需要的文件夹，用排除规则和文件过滤控制范围；减少不必要的后台定时任务，简单任务用 Fast 模式并关闭深度思考。"),
        ("c5,c6", "第三是隐私和可靠性。敏感对话要在第一条消息之前开启 Incognito，记忆有误就直接修改；依赖本机工具的 routine，要确保运行时电脑开机、桌面应用在线；分享 agent 时，记得把它依赖的数据源一起分享。"),
    ],
})

# ----------------------------------------------------------------------------- 03 其他主要功能
SLIDES.append({
    "kind": "cards", "section": S3, "title": "Chat 与 chat agents", "cols": 3,
    "lead": "System chat agent My Assistant 对所有用户默认可用，按每个用户自己的权限访问各类资源。",
    "cards": [
        {"key": "c1", "title": "知识范围", "text": "All data and apps、General knowledge、Specific data and apps 三种模式，可指定具体资源。"},
        {"key": "c2", "title": "Citations 与 Explanations", "text": "编号引用和 Sources 列表；对 dashboards、datasets 提问时附 Explanation：来源、筛选、假设和计算，datasets 另给出 SQL。"},
        {"key": "c3", "title": "Actions 与 Web search", "text": "在对话中调用 Outlook、Jira、PagerDuty 等 actions，执行前校验权限；Web search 需管理员启用后才可用。"},
        {"key": "c4", "title": "Custom chat agents", "text": "Persona instructions 与三种 communication style；Reference documents 最多 10 个文件，逐字常驻上下文；绑定 Spaces 与 actions。"},
        {"key": "c5", "title": "发布与分享", "text": "Update preview 测试后 Launch；Owner / Viewer 权限；管理员允许托管域名后，可生成嵌入代码放到外部网站。"},
        {"key": "c6", "title": "Memory", "text": "记住回答风格、常用资源与职责，仅本人可见，可查看和删除；对话保存 90 天。"},
    ],
    "src": ["chat", "explain", "agents", "custom_agents", "agent_bp"],
    "say": [
        "第三部分快速过一遍其他主要功能。先看 Chat。每个用户默认有一个系统 agent，叫 My Assistant，它按每个用户自己的权限访问各种资源。",
        ("c1,c2,c3", "提问时可以选择知识范围；回答带编号引用，针对仪表板和数据集的问题还会附 Explanation，说明来源、假设和计算方法。对话里可以直接调用 Outlook、Jira 这类动作，网页搜索需要管理员先启用。"),
        ("c4,c5,c6", "针对具体场景，可以创建自定义 chat agent：写 persona 指令、上传参考文档、绑定 Spaces 和动作，预览测试后发布，分享给同事，或者嵌入到外部网站。Chat 还会记住你的偏好，记忆只属于你本人。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S3, "title": "Spaces：团队共享的上下文", "cols": 3, "body_pt": 16, "title_pt": 19,
    "lead": "把一个团队或领域需要的资料和 Quick 资源集中在一起，供成员提问，也可以作为 agent 和 Research 的上下文。",
    "cards": [
        {"key": "s1", "title": "放什么", "bullets": ["Files：文档、音频、视频、代码", "Dashboards、Topics、Knowledge bases、Actions", "同时是 Apps 的数据层"]},
        {"key": "s2", "title": "容量", "bullets": ["每个 space 最多 10,000 个文件、10 GB", "PDF、Word、PPT 单文件 500 MB，其他 50 MB", "每类资源最多挂载 20 个"]},
        {"key": "s3", "title": "权限", "bullets": ["Owner / Viewer，可指定 co-owner", "挂载的资源仍按个人权限控制", "上传的文件对所有成员可见"]},
    ],
    "note": {"label": "典型用法", "text": "汇总客户反馈供团队提问；用团队手册和流程做新人入职；分析数百份年报；从会议录音中检索行动项。"},
    "src": ["spaces", "spaces_manage"],
    "say": [
        ("s1", "Spaces 把一个团队需要的文件、仪表板、Topics、知识库和动作放在一起，供成员提问，也可以作为 agent 和 Research 的上下文。"),
        ("s2,s3", "每个 space 最多一万个文件、10 GB。要注意，挂载的资源仍按个人权限控制，但直接上传的文件，对所有成员都可见。"),
        ("note", "典型用法包括汇总客户反馈、新人入职、分析大量年报，以及从会议录音中检索行动项。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S3, "title": "Quick Sight：BI 加上生成式分析", "cols": 3,
    "lead": "延续 QuickSight 的 BI 能力，并加入自然语言分析；仅在控制台开通的账户中提供。",
    "cards": [
        {"key": "d1", "title": "数据连接与准备", "text": "数据库、数仓、文件和 SaaS 数据源；SPICE 单数据集最多 20 亿行；新的可视化 data preparation 体验。"},
        {"key": "d2", "title": "Topics", "text": "多数据集语义层，最多 12 个 datasets；在 chat 中由 LLM 生成跨数据集 SQL，行级安全（RLS）照常生效。"},
        {"key": "d3", "title": "Dashboard Q&A", "text": "作者发布时勾选 Allow data Q&A，即可对 dashboard 提问，无需单独创建 Topic。"},
        {"key": "d4", "title": "Generate analysis", "text": "一段描述加最多 3 个 datasets 生成多 sheet 的 analysis；也可根据其他 BI 工具的看板截图重建。"},
        {"key": "d5", "title": "Summaries、stories 与 Scenarios", "text": "Executive summaries 总结 dashboard 要点；Data stories 生成叙事报告；Scenarios 拆解多步业务问题。"},
        {"key": "d6", "title": "Embedded analytics", "text": "嵌入 dashboard、单个 visual 或完整 console；匿名嵌入可用 tag-based RLS 隔离租户。"},
    ],
    "src": ["sight", "topics", "dash_qa", "gen_analysis", "scenarios", "stories", "embed"],
    "say": [
        "Quick Sight 延续了 QuickSight 的 BI 能力，只在控制台开通的账户里提供。",
        ("d1,d2,d3", "导入 SPICE 的单个数据集最多 20 亿行。Topics 是最多 12 个数据集的语义层，用户在 chat 里提问时由大模型生成跨数据集的 SQL，行级安全照样生效；只想对某个仪表板提问，作者发布时勾选 Dashboard Q&A 就行。"),
        ("d4,d5,d6", "作者可以用一段描述生成多页分析，甚至根据其他 BI 工具的截图重建看板；读者可以用 Executive summaries、Data stories 和 Scenarios；分析结果还可以嵌入到自己的应用里。"),
    ],
})

SLIDES.append({
    "kind": "flow", "section": S3, "title": "Quick Research：带引用的深度研究",
    "lead": "从 Web、企业数据和第三方数据源收集信息，生成带编号引用、可追溯来源的研究报告。",
    "steps": [
        {"key": "s1", "title": "Research objective", "bullets": ["研究什么、为什么", "行业、地区、时间范围", "关注的指标、竞品与产出形式"]},
        {"key": "s2", "title": "Research materials", "bullets": ["Web search，可设 preferred / avoid 网站", "Files、Spaces、dashboards、knowledge bases、connectors", "第三方数据：FactSet、S&P Global、IDC、US Patents、PubMed"]},
        {"key": "s3", "title": "Review plan", "bullets": ["先看计划草稿", "补充强调点、排除项和领域指引，再开始研究"]},
        {"key": "s4", "title": "报告与迭代", "bullets": ["编号引用可追溯原文", "in-line 或 high level feedback 生成新版本", "导出 PDF / Word，或生成 Executive summary"]},
    ],
    "note": {"label": "两种模式", "text": "Fast 约 4–7 分钟，适合快速洞察；Deep 约 20–30 分钟，适合复杂主题。Research 也可以作为 Flows 的一步按计划运行。"},
    "src": ["research", "research_obj", "research_mat", "third_party", "wn_research_flows"],
    "say": [
        "Quick Research 从网页、企业数据和第三方数据源收集信息，生成带编号引用的研究报告。",
        ("s1,s2", "先写清研究目标，包括范围、时间和关注点；再选材料，除了网页和内部资料，还能接入 FactSet、S&P Global、IDC 等订阅数据，以及美国专利和 PubMed。"),
        ("s3,s4", "开始前先审阅研究计划；报告完成后可以通过引用核对原文，用反馈生成新版本，最后导出 PDF 或 Word。"),
        ("note", "Fast 模式大约 4 到 7 分钟，Deep 大约 20 到 30 分钟。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S3, "title": "自动化：Quick Flows 与 Quick Automate", "cols": 2, "body_pt": 15, "title_pt": 19,
    "lead": "两种自动化工具，面向不同的用户和流程规模。",
    "cards": [
        {"key": "f", "tag": "面向任何业务用户", "title": "Quick Flows", "bullets": [
            "用自然语言描述生成，或从 chat 对话生成（Create Flow from conversation）",
            "步骤：user input、AI responses、data insights、application actions；Reasoning group 处理循环与条件",
            "按日、周、月定时；Pre-built flows 如 Meeting summarizer、Project status reporter"]},
        {"key": "a", "tag": "面向 power users · 仅控制台开通的账户", "title": "Quick Automate", "bullets": [
            "Automation Assistant 先生成高层计划，再生成每步动作",
            "浏览器操作、Excel、PDF、REST API、代码、AWS 服务，以及 Salesforce、SAP 等",
            "按 case 处理，需要判断时创建 HITL 任务；定时或 API 触发，CloudWatch 监控"]},
    ],
    "note": {"label": "怎么选", "text": "Flows 适合个人和团队的较短任务；Automate 适合集中管理、长时间、高量、可独立于个人运行的流程，如发票和贷款申请处理。", "h": 0.8},
    "src": ["automations", "flows", "flows_create", "prebuilt_flows", "automate", "automate_start", "automate_orch", "automate_deploy"],
    "say": [
        "自动化有两个工具。",
        ("f", "Quick Flows 面向业务用户：用自然语言描述，或者从一次对话生成工作流，由用户输入、AI 步骤、数据洞察和应用动作组成，可以按日、周、月定时运行，系统还预置了会议纪要、项目状态报告等 flow。"),
        ("a", "Quick Automate 面向高级用户，只在控制台开通的账户里提供：Assistant 先生成高层计划，再生成每一步的动作，覆盖浏览器、Excel、API、代码和各类企业系统；需要人判断时创建人工任务，可以定时或通过 API 触发。"),
        ("note", "官方给的选择依据是：Flows 适合个人和团队的较短任务；Automate 适合集中管理、长时间、高量、可以不依赖某个人运行的流程。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S3, "title": "Apps in Amazon Quick：用一段话生成 Web 应用", "cols": 3, "body_pt": 15.5, "title_pt": 19,
    "lead": "描述用途、受众和所需数据，agent 实时生成可交互的 Web 应用，迭代后发布给组织使用；2026-09-01 正式发布。",
    "cards": [
        {"key": "a1", "title": "能构建什么", "bullets": ["dashboards、内部工具、数据录入、知识门户与 FAQ", "内置 AI inference 与 key-value storage", "嵌入 Quick Sight visuals，以及以 space 为知识的 chat"]},
        {"key": "a2", "title": "数据与集成", "bullets": ["直连 Quick datasets，按查看者身份实时查询，RLS / CLS 照常生效", "100 多个预置 connectors，或用 REST、OpenAPI、MCP 自建"]},
        {"key": "a3", "title": "安全与发布", "bullets": ["沙箱运行，外部访问只能经平台接口或 connectors", "每个集成需作者批准，区分读和写", "一键发布，按 Co-owner / Viewer 分享"]},
    ],
    "note": {"label": "流程", "text": "Describe → Generate → Preview → Iterate → Publish；每次修改自动生成版本，可回滚，不影响已发布版本。"},
    "src": ["apps", "apps_build", "apps_data", "apps_sec", "wn_apps_ga"],
    "say": [
        "Apps 在 9 月正式发布：用自然语言描述用途、受众和数据，agent 实时生成一个可交互的 Web 应用。",
        ("a1,a2", "可以做看板、内部工具、数据录入和知识门户；应用可以直连 Quick 数据集，按每个查看者的身份实时查询，也可以通过一百多个预置连接器读写外部系统。"),
        ("a3,note", "应用运行在沙箱里，每个集成都要作者批准；每次修改都自动生成版本，可以回滚，发布一键完成。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S3, "title": "Integrations 与 Extensions", "cols": 2, "body_pt": 13.5,
    "lead": "Knowledge bases 同步企业内容供 AI 检索，Connectors 实时调用外部系统，Extensions 把 Quick 嵌进日常工具。",
    "cards": [
        {"key": "k1", "title": "Knowledge bases", "text": "S3、SharePoint、OneDrive、Confluence、Google Drive、Web Crawler，默认每天同步；前五种支持文档级 ACL（创建时启用），按已同步的文档权限过滤，无法评估权限时不返回文档。"},
        {"key": "k2", "title": "Connectors", "text": "60 多项内置集成（Microsoft 365、Atlassian、Salesforce、SAP 等）；也可用 OpenAPI、REST API 或远程 MCP server 自建，支持经 VPC 访问私有 MCP server。"},
        {"key": "k3", "title": "复用已有投资", "text": "接入现有的 Amazon Q Business index、Amazon Bedrock 托管 knowledge base（支持跨账户），或 AWS Agent Registry 中登记的 MCP server。"},
        {"key": "k4", "title": "Extensions", "text": "浏览器（Chrome、Firefox、Edge）、Outlook、Excel、Word、PowerPoint、Slack、Microsoft Teams；Microsoft 365 extensions 于 2026-08-17 GA。"},
    ],
    "note": {"label": "注意", "text": "用户触发的动作用本人的 OAuth 凭证，自动化流程用服务级凭证；Slack 和 Teams 公共频道中的回答基于提问者本人的权限，部署前需评估。", "h": 0.8},
    "src": ["integrations", "supported_int", "kb", "acl_bp", "mcp", "byoi", "byo_bedrock", "registry", "extensions",
            "actions_how", "slack_admin", "teams_admin", "wn_m365"],
    "say": [
        "再看集成。",
        ("k1", "Knowledge bases 同步 S3、SharePoint、Confluence 等企业内容，支持文档级权限：每次检索按从源系统同步来的权限过滤，部分集成还会实时复核，无法评估权限时就不返回文档。"),
        ("k2,k3", "Connectors 有 60 多项内置集成，也可以用 OpenAPI 或远程 MCP server 自己接入，包括 VPC 里的私有 MCP server；已有 RAG 投入的企业，可以直接接入 Q Business 索引或 Bedrock 知识库。"),
        ("k4", "Extensions 把 Quick 嵌进浏览器、Outlook、Excel、Word、PowerPoint、Slack 和 Teams。"),
        ("note", "要注意，在 Slack 和 Teams 的公共频道里，回答基于提问者本人的权限，可能让其他成员看到无权查看的内容，部署前要评估。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S3, "title": "安全与治理", "cols": 3,
    "lead": "Quick 运行在 AWS 上，沿用安全团队已经认可的身份、网络和合规控制。",
    "cards": [
        {"key": "g1", "title": "身份与权限", "text": "IAM Identity Center、AD、IAM federation；Custom permissions 按账户、角色、用户收窄能力；Deny by Default 让新 AI 功能默认关闭。"},
        {"key": "g2", "title": "Human in the loop", "text": "connector 所有者可把写操作设为 Always Ask（用户不能覆盖）；Smart Approvals 自动放行低风险动作，后果性动作转人工（desktop 与 mobile app）。"},
        {"key": "g3", "title": "Approval workflows 与 limit profiles", "text": "Spaces、knowledge bases、custom chat agents 的共享可要求审批；limit profiles 按用户限制索引存储和 agent hours。"},
        {"key": "g4", "title": "Data loss prevention", "text": "接入 Microsoft Purview 敏感度标签，对 Chat、Spaces、knowledge bases 中的文件执行 Block / Warn / Allow。"},
        {"key": "g5", "title": "审计与监控", "text": "Chat、feedback、agent hours、DLP 等 vended logs 投递到 CloudWatch Logs、S3 或 Firehose；CloudTrail 记录 API 活动。"},
        {"key": "g6", "title": "数据保护", "text": "不使用客户数据训练模型；静态与传输加密，可用客户托管 KMS 密钥；Bedrock Guardrails 过滤有害内容。"},
    ],
    "src": ["custom_perm", "deny_default", "smart", "approval", "limits", "dlp", "logs", "data_prot", "cmk", "guardrails"],
    "say": [
        "企业治理方面，Quick 沿用 AWS 的身份、网络和合规控制。",
        ("g1,g2,g3", "Custom permissions 可以在账户、角色、用户三级收窄能力，Deny by Default 让新的 AI 功能默认关闭；写操作可以强制人工确认；Spaces、知识库和 agent 的共享可以走审批；limit profiles 按用户限制用量。"),
        ("g4,g5,g6", "数据防泄漏可以接入 Microsoft Purview 敏感度标签；日志可以投递到 CloudWatch Logs、S3 或 Firehose；AWS 不使用客户数据训练模型，并支持客户托管的 KMS 密钥。"),
    ],
})

# ----------------------------------------------------------------------------- 04 应用场景
SLIDES.append({
    "kind": "cards", "section": S4, "title": "按部门的应用场景（均来自 AWS 官方描述）", "cols": 4, "body_pt": 13, "title_pt": 17,
    "cards": [
        {"key": "c1", "title": "Sales", "bullets": ["客户研究与会前准备", "Research 生成 account plan，再更新 Salesforce 商机", "线索打分与个性化外联"]},
        {"key": "c2", "title": "Marketing", "bullets": ["对话式分析活动效果", "Research + Spaces 快速出竞品报告", "一次生成简报、演示稿和邮件序列"]},
        {"key": "c3", "title": "Finance", "bullets": ["报告生成与预算分析", "Quick Automate 处理发票与对账", "Excel extension 搭建财务模型"]},
        {"key": "c4", "title": "HR", "bullets": ["入职 agent：HR space + knowledge base + actions", "通过 Visier 分析 headcount、attrition 与 tenure"]},
        {"key": "c5", "title": "Operations", "bullets": ["监控库存与履约的应用", "自主 agent 全天候处理采购订单", "监控包装法规变化"]},
        {"key": "c6", "title": "Legal", "bullets": ["合同跟踪，在 Word extension 中审阅合同", "合规工作流", "批量检查租约合规"]},
        {"key": "c7", "title": "IT 与工程", "bullets": ["对话中创建 Jira 工单、ServiceNow incident", "结合 PagerDuty、New Relic 做事件分诊", "桌面版经 ACP 把开发任务交给 coding agents"]},
        {"key": "c8", "title": "Customer service", "bullets": ["领域 agent 作为认证资产发布", "把 Embedded Chat 嵌入 CRM 或客服控制台"]},
    ],
    "src": ["faqs", "blog_sales", "wn_research_flows", "blog_marketing", "wn_m365", "blog_onboarding", "blog_autonomous",
            "blog_lease", "blog_newrelic", "coding_agents", "enterprise", "wn_ga"],
    "say": [
        "进入第四部分，应用场景。这一页按部门整理了 AWS 官方描述过的场景。",
        ("c1,c2", "销售可以做客户研究和会前准备，用 Research 生成客户账户计划，再更新 Salesforce 商机；市场团队可以用对话分析活动效果，快速出竞品报告。"),
        ("c3,c4", "财务可以用 Automate 处理发票和对账，用 Excel 扩展搭财务模型；人力资源可以做入职助手，或者接入 Visier 分析人数、离职和司龄。"),
        ("c5,c6", "运营可以用应用监控库存和履约，让自主 agent 全天候处理采购订单；法务可以在 Word 里审阅合同，批量检查租约合规。"),
        ("c7,c8", "IT 团队可以在对话里建 Jira 工单和 ServiceNow 事件，结合 PagerDuty、New Relic 做事件分诊；客服团队可以把聊天助手嵌入 CRM 和客服控制台。"),
    ],
})

SLIDES.append({
    "kind": "quotes", "section": S4, "title": "客户案例",
    "lead": "数字与表述来自 AWS 客户页和博客，中文为要点转述。",
    "quotes": [
        {"company": "Jabil", "who": "制造与供应链", "quote": "Quick Automate 优化了应收账款催收和 RFQ 提交，提升报价准确度，废料减少 10%，每年节省约 40 万美元。", "use": "Quick Automate · Quick Sight · Quick Research"},
        {"company": "GoDaddy", "who": "互联网", "quote": "从原有 BI 迁移到 Quick：看板渲染从 15 分钟降到 5 秒以内，看板数量减少 50%，每年节省超过 15,000 小时。", "use": "Quick Sight · chat agents · Quick Flows"},
        {"company": "Kitsa", "who": "临床试验", "quote": "用 UI agent 从数十万个网站抽取临床试验站点数据：抽取覆盖率 96%，成本比原人工流程降低 91%。", "use": "Quick Automate"},
        {"company": "Aderant", "who": "法律软件 · 云运维团队", "quote": "统一搜索 6 个厂商系统，用 Flow 生成知识库文章：搜索提速 90%，文档编写提速 75%。", "use": "Spaces · Quick Flows"},
    ],
    "src": ["enterprise", "blog_godaddy", "blog_kitsa", "blog_aderant"],
    "say": [
        "再看几个客户案例，数字都来自 AWS 的客户页和博客。",
        ("q1,q2", "制造业的 Jabil 用 Quick Automate 优化应收账款催收和报价请求提交，废料减少 10%，每年节省约 40 万美元。GoDaddy 从原来的 BI 迁移到 Quick，看板渲染从 15 分钟降到 5 秒以内，每年节省超过一万五千小时。"),
        ("q3,q4", "临床试验领域的 Kitsa 用 Quick Automate 的 UI agent 从几十万个网站抽取数据，覆盖率 96%，成本降低 91%。法律软件公司 Aderant 的云运维团队统一搜索 6 个厂商系统，搜索提速 90%。"),
    ],
})

# ----------------------------------------------------------------------------- 05 最佳实践
SLIDES.append({
    "kind": "table", "section": S5, "title": "功能选型：什么任务用什么",
    "lead": "根据官方对各功能的定位整理。",
    "head": ["需求", "首选功能", "要点"], "widths": [3.0, 2.9, 6.2], "pt": 14, "hpt": 14.5,
    "rows": [
        ["临时提问、生成文档", "Chat / My Assistant", "选好知识范围，用引用和 Explanation 核对结论"],
        ["个人日常工作与定时任务", "Quick 桌面版", "Activity feed、routines、本地文件、local MCP 与 coding agents"],
        ["固定口径的团队助手", "Custom chat agent + Spaces", "必须逐字遵守的规则放进 reference documents"],
        ["带引用的深度调研", "Quick Research", "时间紧用 Fast，复杂主题用 Deep；可放进 Flows 定期运行"],
        ["重复的个人与团队任务", "Quick Flows", "无代码；按日、周、月定时；定时运行时为写操作保留人工确认"],
        ["跨系统、高量、无人值守流程", "Quick Automate", "case 管理、异常处理、HITL；定时或 API 触发"],
        ["交互式内部工具", "Apps in Amazon Quick", "直连 datasets 与 connectors；一次只改一处，记下稳定版本"],
        ["指标分析与看板", "Quick Sight + Topics", "先做 dataset enrichment，再建 Topics"],
    ],
    "src": ["chat", "desktop", "agent_bp", "research_obj", "automations", "flows_sched", "apps_tips", "topics"],
    "say": [
        "最后一部分是最佳实践。第一条是选对功能。",
        ("r1,r2,r3", "临时提问和生成文档，直接用 Chat；个人的日常工作和定时任务，用桌面版的 feed 和 routine；需要固定口径的团队助手，就建自定义 agent，配上 Spaces。"),
        ("r4,r5,r6", "深度调研用 Research；重复的个人和团队任务用 Flows；跨系统、高量、需要无人值守的流程用 Automate。"),
        ("r7,r8", "交互式的内部工具用 Apps；指标分析和看板用 Quick Sight 加 Topics，并先把数据集的元数据补全。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S5, "title": "agent 与知识的最佳实践", "cols": 3,
    "lead": "官方把 custom chat agent 的上下文分成三类，用途不同；结构化数据问答的质量取决于元数据。",
    "cards": [
        {"key": "c1", "tag": "Context ①", "title": "Persona instructions", "text": "写高层的行为、目标和资源使用方式；会被 AI 扩写和改写，适合通用、探索性的 agent。"},
        {"key": "c2", "tag": "Context ②", "title": "Reference documents", "text": "逐字保留，是 agent 的“操作手册”：品牌口径、固定顺序的多步流程、回答模板。"},
        {"key": "c3", "tag": "Context ③", "title": "Spaces", "text": "动态知识层：持续更新、多人维护的内容，实时 dashboards 与 datasets，沿用已有权限边界。"},
        {"key": "c4", "tag": "数据", "title": "Dataset Enrichment", "text": "把列描述、同义词、单位、口径和业务规则写进数据集元数据，再加入 Topic。"},
        {"key": "c5", "tag": "数据", "title": "Topics 建模", "text": "从星型模型开始；Topic 级 custom instructions 只写跨数据集逻辑；在 Explanation 中检查生成的 SQL。"},
        {"key": "c6", "tag": "发布", "title": "先预览再发布", "text": "每次修改先 Update preview 测试再 Launch；分享后的每次 Launch 都会影响所有有权访问的用户。"},
    ],
    "src": ["agent_bp", "custom_agents", "enrich", "topics", "topics_rel", "topics_ci"],
    "say": [
        "第二条是设计好 agent 的上下文，官方把它分成三类。",
        ("c1,c2,c3", "Persona 指令写高层的行为和目标，会被 AI 扩写和改写，适合通用的 agent；参考文档逐字保留，相当于操作手册，品牌口径和固定流程放在这里；Spaces 是动态知识层，适合持续更新的内容，并沿用已有的权限边界。"),
        ("c4,c5,c6", "结构化数据的问答质量取决于元数据：先给数据集补上列描述、同义词和业务规则，再加入 Topic，并在 Explanation 里检查生成的 SQL。每次修改 agent 都先预览测试再发布。"),
    ],
})

SLIDES.append({
    "kind": "cards", "section": S5, "title": "集成、安全与成本的最佳实践", "cols": 3,
    "lead": "摘自官方安全最佳实践、knowledge base ACL 最佳实践、Smart Approvals 与 limit profiles 文档。",
    "cards": [
        {"key": "b1", "title": "先定难以更改的事项", "text": "需要客户托管密钥时，先注册 KMS 密钥再创建任何资源；身份模型事后难以更改；knowledge base 的 ACL 设置创建后不可更改。"},
        {"key": "b2", "title": "最小权限", "text": "优先用户级 OAuth；共享的服务凭证收窄范围；SharePoint 用 Sites.Selected；按 connector 限制创建、共享和使用。"},
        {"key": "b3", "title": "高风险动作强制确认", "text": "必须人工批准的写操作设为 Always Ask，不依赖自动审查；用不到的工具直接禁用。"},
        {"key": "b4", "title": "分阶段放开 AI 功能", "text": "对 AI 类启用 Deny by Default，新功能先在开发或预发账户验证；不允许无人值守时在账户级限制 Automate、Flows。"},
        {"key": "b5", "title": "尽早接日志", "text": "大规模上线前配置 vended logs（不回溯）；chat logs 可能含个人信息，用 CloudWatch Logs masking policies 屏蔽。"},
        {"key": "b6", "title": "控制用量与成本", "text": "一个组织一个 Quick 账户；用 limit profiles 设置每用户上限；在下个计费周期开始前移除不再需要的用户。"},
    ],
    "src": ["sec_bp", "cmk", "acl_bp", "smart", "tool_perm", "deny_default", "logs", "acct", "limits", "billing"],
    "say": [
        "第三条是集成、安全和成本。",
        ("b1,b2,b3", "先把难以更改的事项定下来：需要客户托管密钥，就在创建任何资源之前注册；身份模型事后很难更改；知识库的 ACL 设置创建后不能再改。权限上优先用户级 OAuth，共享凭证要收窄范围；必须人工批准的写操作，要在连接器上设为每次询问。"),
        ("b4,b5,b6", "有变更审批要求的组织，可以启用 Deny by Default，新功能先在预发账户验证；日志要尽早接，因为投递不回溯。成本上，一个组织用一个 Quick 账户，用 limit profiles 给每个用户设上限，不再需要的用户在下个计费周期前移除。"),
    ],
})

SLIDES.append({
    "kind": "flow", "section": S5, "title": "建议的上手路径",
    "lead": "从小范围、可衡量的场景开始，边用边补齐治理。",
    "steps": [
        {"key": "s1", "title": "试用", "bullets": ["控制台开通 30 天试用，最多 25 个用户", "先定身份模型、home Region、是否使用客户托管密钥"]},
        {"key": "s2", "title": "接入与治理", "bullets": ["添加 desktop connector 开通桌面访问，用 MDM 分发", "连接 1–2 个核心 knowledge bases 和常用 connectors", "配置 custom permissions、日志与 limit profiles"]},
        {"key": "s3", "title": "试点 2–3 个场景", "bullets": ["桌面版 Morning brief / Meeting prep routine", "团队 agent + Spaces、一个 flow", "记录节省的时间"]},
        {"key": "s4", "title": "推广", "bullets": ["发布验证过的 agents、skills 与 flows", "开启共享审批", "需要无人值守的流程再引入 Automate"]},
    ],
    "note": {"label": "说明", "text": "这是基于官方能力和最佳实践整理的建议路径，不是 AWS 的官方方法论；试用条款以开通页面为准。"},
    "src": ["signup", "pricing", "desktop_ent", "sec_bp", "limits", "approval"],
    "say": [
        "最后给一个建议的上手路径。这是根据官方能力和最佳实践整理的建议，不是 AWS 的官方方法论。",
        ("s1,s2", "第一步试用：通过控制台开通 30 天试用，开通前先定好身份模型、主区域和是否使用客户托管密钥。第二步接入和治理：添加 desktop connector 开通桌面访问，再用 MDM 分发应用，连上一两个核心知识库和常用连接器，同时配好权限、日志和用量上限。"),
        ("s3,s4", "第三步试点两到三个场景，比如桌面版的晨间简报和会前准备，一个团队 agent 加 space，一个 flow，并记录节省的时间。第四步推广：发布验证过的 agent、skill 和 flow，开启共享审批，需要无人值守的流程再引入 Automate。"),
    ],
})

REF_KEYS = ["whatis", "how", "pricing", "plans", "desktop_home", "desktop", "desktop_interface", "chat_desktop", "feed",
            "agents_desktop", "mission", "skills", "connections_desktop", "coding_agents", "system_tools", "knowledge_desktop",
            "memories", "kg", "brand", "desktop_sec", "desktop_ent", "desktop_mdm", "usage_desktop", "mobile_home", "smart",
            "chat", "custom_agents", "agent_bp", "spaces", "sight", "topics", "research", "automations", "apps",
            "integrations", "extensions", "custom_perm", "sec_bp", "blog_desktop_ga", "wn_desktop_ga"]

SLIDES.append({
    "kind": "refs", "section": "参考资料", "title": "主要参考资料（AWS 英文官方文档）", "refs": REF_KEYS, "pt": 12,
    "say": ["主要参考资料列在这一页，全部是 AWS 英文官方文档和博客；每一页底部也标注了对应的来源链接。"],
})

SLIDES.append({
    "kind": "end", "title": "总结",
    "items": [
        {"key": "e1", "title": "一个入口", "text": "以 Chat 为中心，agents、Spaces 与 Integrations 组合出研究、自动化、分析和应用"},
        {"key": "e2", "title": "桌面版是重点", "text": "Activity feed、routines、Skills、local MCP 与 coding agents，让 agent 主动干活"},
        {"key": "e3", "title": "企业级治理", "text": "权限收窄、human in the loop、共享审批、DLP、日志与客户托管密钥"},
        {"key": "e4", "title": "从小处开始", "text": "先试点高频、可衡量的场景，再随治理完善逐步推广"},
    ],
    "say": [
        ("e1", "总结一下。Amazon Quick 以 Chat 为中心，用 agent、Spaces 和集成，组合出研究、自动化、数据分析和应用构建这些能力。"),
        ("e2", "桌面版是其中的重点：Activity feed、routine、Skills、本地 MCP 和 coding agent，让 agent 从回答问题变成主动替你干活。"),
        ("e3", "在企业治理上，它提供权限收窄、人在回路、共享审批、数据防泄漏、日志和客户托管密钥。"),
        ("e4", "落地时，建议从高频、可衡量的小场景开始，再随着治理能力的完善逐步推广。谢谢大家。"),
    ],
})
