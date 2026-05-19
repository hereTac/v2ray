import requests
import re

def main():
    # 获取 README.md 的原始内容
    url = "https://raw.githubusercontent.com/asdsadsddas123/freevpn/main/README.md"
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    content = resp.text

    # 提取“免费高速节点”部分
    pattern = r"免费高速节点[\s\S]*?(```[\s\S]*?```)?([\s\S]+?)#?\s*\w*VPN"  # 尝试定位
    # 但实际内容中“免费高速节点”后面直接是节点链接
    # 所以直接用正则提取所有节点链接
    node_pattern = r'(?m)^(ss|vless|trojan|hysteria2|vmess)://[^\s]+'
    nodes = re.findall(node_pattern, content)

    # 也可以直接提取所有节点行
    node_lines = re.findall(r'^(ss://[^\s]+|vless://[^\s]+|trojan://[^\s]+|hysteria2://[^\s]+|vmess://[^\s]+)', content, re.MULTILINE)

    #print("免费高速节点（共{}条）：".format(len(node_lines)))

    with open("output_nodes.txt", "w", encoding="utf-8") as f:
        for node in node_lines:
            f.write(node + "\n")
    print(f"已将 {len(node_lines)} 条节点写入 output_nodes.txt")

if __name__ == "__main__":
    main()
