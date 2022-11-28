import yaml

with open("params.yaml") as f:
    params = yaml.safe_load(f)

# 値の読み込み
name = params['Type']
radius = params['Radius']
temperature = params['Temperature']

# 型の確認
print(f"name: {name} ({type(name)})")
print(f"radius: {radius} ({type(radius)})")
print(f"name: {temperature} ({type(temperature)})")

# ファイルへの出力
with open("output.txt", "w") as f:
    f.write(f"name = {name}\n")
    f.write(f"radius = {radius}\n")
    f.write(f"temperature = {temperature}\n")

print("Generated output.txt")
