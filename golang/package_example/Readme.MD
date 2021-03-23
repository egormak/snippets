## Init Go MoD
В каждом пакете необходимо провести инициализацию go mod: `go mod init <domain>/<name_package>`

```shell
go mod init example.com/hi
```
Для работы в одной дириктории можно воспользоватся командой: `go mod edit -replace=<domain>/<name_package>=../<name_package>`
```shell
go mod edit -replace=example.com/greetings=../greetings
```

Указать все зависимости: `go mod tidy`