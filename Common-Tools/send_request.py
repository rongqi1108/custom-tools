import requests
import json

url = "https://mytan.maiseed.com.cn/api/v2/messages"
headers = {
    "Authorization": "Bearer d1c0a742631301adbcdd63fae4e46441577ce477194e97cd2054497084fa0c6c",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Origin": "https://mytan.maiseed.com.cn",
    "Referer": "https://mytan.maiseed.com.cn/chat",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
}
text = """Execution* CPUBackend::onCreate(const std::vector<Tensor*>& inputs, const std::vector<Tensor*>& outputs,
                                const MNN::Op* op) {
    /**
     * BatchNorm it will be converted to scale
     * for model convert, don't print error log
     */
    if (op->type() == OpType_BatchNorm) {
        return nullptr;
    }
    auto opType = op->type();
    if (!outputs.empty()) {
        if (TensorUtils::getDescribe(outputs[0])->quantAttr != nullptr && 
            TensorUtils::getDescribe(outputs[0])->type == DataType_DT_INT8) {
            opType = _getRealOpType(opType);
        }
    }

    // TODO: rm this convert when merge diff datatyoe of op
    auto map  = gCreator;
    auto iter = map->find(opType);
    if (iter == map->end()) {
        MNN_PRINT("Don't support type [%s]\n", MNN::EnumNameOpType(op->type()));
        return nullptr;
    }
    Execution* exe = nullptr;
    bool needCast = false;
    if (exe == nullptr) {
        exe = iter->second->onCreate(inputs, outputs, op, this);
    }
    return exe;
}"""
data = {
    "content": [{"type": "text", "text": text}],
    "stream": True,
    # "conversation": {"title": "介绍一下自己", "model": "gpt-4o"}
    "conversation_id":"67a97091edbfb27918d88e50"
}

response = requests.post(url, headers=headers, json=data, stream=True)

# 用于存储所有文本内容的变量
full_text = ""

for line in response.iter_lines():
    if line:
        try:
            # 移除前缀 'data: ' 并解析 JSON 数据
            line_str = line.decode('utf-8')
            if line_str.startswith('data: '):
                json_data = json.loads(line_str[6:])
                # 提取 content 字段中的文本内容
                if 'choices' in json_data and json_data['choices']:
                    text_content = json_data['choices'][0]['delta'].get('content', '')
                    full_text += text_content
        except json.JSONDecodeError:
            # print("Invalid JSON format:", line_str)
            print("")

# 打印所有集中到一起的文本内容
print(full_text)