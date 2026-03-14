# ai_git servers

## 运行 `issue_server.py`

这个服务基于 Python 标准库 `http.server`，没有额外依赖。

在项目根目录执行：

```bash
python3 servers/issue_server.py
```

启动成功后会监听：

```text
http://0.0.0.0:8089
```

终端会输出：

```text
Listening on http://0.0.0.0:8089
```

## 接口说明

- 方法：`POST`
- 路径：`/issue`
- 端口：`8089`
- 请求体：JSON

示例请求：

```bash
curl -X POST http://127.0.0.1:8089/issue \
  -H "Content-Type: application/json" \
  -d '{"title":"demo issue","text":"hello"}'
```

示例响应：

```text
recv demo issue
```

## 返回规则

- 当路径不是 `/issue` 时，返回 `404 not found`
- 当 `Content-Length` 非法时，返回 `400 invalid content length`
- 当请求体不是合法 JSON 时，返回 `400 invalid json`
- 当请求正常时，返回 `200 recv <title>`

## 停止服务

在启动服务的终端里按 `Ctrl+C` 即可停止。
