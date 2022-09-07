def foncyaml():
    import yaml
    with open("yaml_file.yaml", "r") as monficyam:
        print(yaml.load(monficyam))

        