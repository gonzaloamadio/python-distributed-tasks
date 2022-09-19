Repo following course: https://www.udemy.com/course/distributed-tasks-demystified-with-celery-python/

# Usage

* Create a virtual environment with python 3.5+
* pip install requirements.txt
* Intall redis and redis desktop manager

```
❯ brew install redis
Running `brew update --auto-update`...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
gdrive-downloader                   got                                 liburing                            llvm@14                             mailsy                              quilt-installer                     weasyprint
==> New Casks
sanesidebuttons                                                                                                                 whist-browser

==> Downloading https://ghcr.io/v2/homebrew/core/redis/manifests/7.0.4
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/redis/blobs/sha256:38c669f105a76cccf7567b4ee32dba6972c63daaf7b4c178e1f79988f846684b
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:38c669f105a76cccf7567b4ee32dba6972c63daaf7b4c178e1f79988f846684b?se=2022-09-19T12%3A40%3A00Z&sig=ZCnMc6VyTL3bVHgQXP5wd5wEYmaiqWpQr7g6rhvhkWQ%3D&sp=r&spr=https&sr=b&sv=20
######################################################################## 100.0%
==> Pouring redis--7.0.4.catalina.bottle.tar.gz
==> Caveats
To restart redis after an upgrade:
  brew services restart redis
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/redis/bin/redis-server /usr/local/etc/redis.conf
==> Summary
🍺  /usr/local/Cellar/redis/7.0.4: 14 files, 2.6MB
==> Running `brew cleanup redis`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

```
brew install --cask another-redis-desktop-manager
==> Downloading https://github.com/qishibo/AnotherRedisDesktopManager/releases/download/v1.5.8/Another-Redis-Desktop-Manager.1.5.8.dmg
==> Downloading from https://objects.githubusercontent.com/github-production-release-asset-2e65be/164574693/c7313403-7db9-40c5-a3b6-dde069913f3d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220919%2Fus-east-1%2Fs3%2Faws4_req
######################################################################## 100.0%
==> Installing Cask another-redis-desktop-manager
==> Moving App 'Another Redis Desktop Manager.app' to '/Applications/Another Redis Desktop Manager.app'
🍺  another-redis-desktop-manager was successfully installed!

```

Celery is an in-memory DB and uses with celery acts as a broker for the queues.
