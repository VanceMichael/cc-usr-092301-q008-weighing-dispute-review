# 水产称重争议复核

这是虾蟹称重服务的 Flask 后端基线，现有健康接口可直接验证，后续领域能力可沿 HTTP 接口扩展。

## 本地验证

执行测试：

```bash
python3 -m pytest -q
```

执行编译或构建检查：

```bash
python3 -m compileall -q app.py tests
```

所有验证均在单个 Linux 应用环境中完成，不需要浏览器或独立运行的数据库、缓存与消息队列。
