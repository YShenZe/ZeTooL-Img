# ZeTooL-Img

ZeTooL-Img 是一个用于爬取网页中的图片和视频链接的 Python 脚本。它支持随机 User-Agent、IP 伪装、重试策略，并能将爬取到的媒体链接保存到 `media_links.txt` 文件中。

## 功能特点

- **随机 User-Agent 和 IP**（使用 `fake_useragent`）。
- **智能重试机制**（基于 `requests`）

## 依赖环境

请确保你的 Python 版本为 3.x，并安装了以下依赖：

```bash
pip install requests beautifulsoup4 pyfiglet fake-useragent colorama
```

## 使用方法

1. **运行脚本**：

   ```bash
   python script.py
   ```

2. **输入要爬取的网页链接**：

   ```plaintext
   请输入要爬取的链接: https://example.com
   ```

3. **脚本将自动解析并输出爬取到的图片和视频链接**：

   ```plaintext
   [Fetch Log] Image Link: https://example.com/image1.jpg
   [Fetch Log] Video Link: https://example.com/video.mp4
   ```

4. **所有爬取到的链接将被保存到 `media_links.txt` 文件中**。

## 许可证

本项目采用 MIT 许可证。自由使用和修改，但请保持原作者信息。

---

**佛祖保佑，永无 bug！**