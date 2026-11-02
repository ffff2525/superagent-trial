# superagent-trial

superagent-trial 是一个小型静态 Web 演示仓库，提供从正整数 N 倒数到 1 的倒计时页面。

## 在线演示

<https://ffff2525.github.io/superagent-trial/>

## 功能

- 输入 1–999 之间的正整数 N，点击“开始”后从 N 依次倒数到 1，最后显示 `Liftoff!`。
- 空值、0、负数、非数字或超过 999 的输入会显示对应的中文错误提示，不会启动倒计时。
- 只使用原生 HTML、CSS 和 JavaScript，不依赖前端框架、构建步骤或外部资源。
- 适配桌面与移动端，并遵循系统的“减少动态效果”偏好。

## 项目结构

```text
.
├── .github/
│   ├── screenshots/          # 演示页截图
│   └── workflows/
│       └── deploy-pages.yml  # GitHub Pages 部署工作流
├── docs/
│   └── index.html            # 倒计时演示页（Pages 根目录）
└── README.md
```

## 本地预览

直接用浏览器打开 `docs/index.html` 即可，无需安装依赖。

如需通过本地 HTTP 服务预览，可在仓库根目录运行任意静态文件服务器，例如：

```console
$ npx serve docs
```

## 部署

推送到 `main` 分支后，`.github/workflows/deploy-pages.yml` 会自动将 `docs/` 目录部署到 GitHub Pages。

首次启用时，请在仓库的 **Settings → Pages** 中将 **Source** 设为 **GitHub Actions**。

## 说明

演示最多支持 999，以保证动画时长和页面流畅度。
