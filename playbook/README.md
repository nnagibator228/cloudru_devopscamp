# Playbook для конфигурации хоста

Для запуска нужно:

1. Заполнить переменные в vault-файле secrets.yaml *(пароль от имеющегося - 1111)*
```
cloudru_password: <пароль пользователя cloudru>
ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfrfE0OluoNHb5dOpV4RpWmVXvMBWc17kaM7DDjCm>
```

2. Заполнить имя хоста и пользователя для исполнения playbook-а в inventory-файле hosts

3. Запустить playbook командой:
```
ansible-playbook -i ./hosts --ask-vault-pass setup_host.yaml
```
