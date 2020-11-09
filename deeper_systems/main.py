import json


def main():
    with open('source_file_2.json') as f:
        data = json.load(f)
    managers = {}
    watcher = {}
    for d in data:
        project_name = d['name']
        priority = d['priority']
        for m in d['managers']:
            if m not in managers.keys():
                managers[m] = []
            managers[m].append((project_name, priority))
        for w in d['watchers']:
            if w not in watcher.keys():
                watcher[w] = []
            watcher[w].append((project_name, priority))

    for m in managers.keys():
        managers[m] = sorted(managers[m], key=lambda x: x[1])
        managers[m] = [p for (p, _) in managers[m]]

    for w in watcher.keys():
        watcher[w] = sorted(watcher[w], key=lambda x: x[1])
        watcher[w] = [p for (p, _) in watcher[w]]

    with open('managers.json', 'w') as fout:
        json.dump(managers, fout, indent=4)
    with open('watchers.json', 'w') as fout:
        json.dump(watcher, fout, indent=4)


if __name__ == "__main__":
    print('[INFO] Doing')
    main()
    print('[INFO] Done.')
