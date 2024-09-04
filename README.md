## mp3looper README

A simple script to loop play a directory of files in 

## Prereqs

- python 3.11
- mpg321 installed
- Running Raspbian GNU/Linux 12 (bookworm) 

## インストール方法

1. USERNAMEとしてログイン
2. mkdir mp3looper
3. `mp3looper` に `cli.py`を作成
4.  `/lib/systemd/system/mp3looper.service`を作成
    ```
    sudo vim /lib/systemd/system/mp3looper.service  # 上記の内容を入れて保存
    ```
    
5.  権限を更新
    ```
    sudo chmod 644 /lib/systemd/system/mp3looper.service
    ```
    
6.  systemdを設定
    
    ```
    sudo systemctl daemon-reload
    sudo systemctl enable mp3looper.service
    ```


### systemd service file

`/lib/systemd/system/mp3looper.service`

```
 [Unit]
 Description=MP3Looper Music Service
 After=multi-user.target

 [Service]
 Type=idle
 User=USERNAME
 Environment="PULSE_RUNTIME_PATH=/run/user/1000/pulse"
 ExecStart=python /home/USERNAME/mp3looper/cli.py --directory /home/USERNAME/Music

 [Install]
 WantedBy=multi-user.target
```

> NOTE: Assumes user id is "1000" 
> Environment is needed to play sound as a systemd service

