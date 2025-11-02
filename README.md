# Dropbox ↔ Moodle Sync Tool

A Python script to sync course materials from **Dropbox** to a local folder and generate update reports / ZIPs for upload to Moodle.

---

## 🔧 How to Run

### 1️⃣ Clone the project
```bash
git clone https://github.com/AhmadEgbaria1/CSCourseSync.git
cd CSCourseSync

2#Create a virtual environment

python -m venv .venv
.venv\Scripts\activate     # on Windows


3#Install dependencies
pip install -r requirements.txt

4#Set your Dropbox credentials
DROPBOX_APP_KEY=your_app_key
DROPBOX_APP_SECRET=your_app_secret
DROPBOX_REFRESH_TOKEN=your_refresh_token

5#Initialize the sync folder

python dropbox_sync.py init --dropbox-folder "/Courses/Algo2025" --mirror "./mirror_algo2025" --config "./sync_config.yaml"

6#preview sync

python dropbox_sync.py sync --mirror "./mirror_algo2025" --report "./reports" --dry-run


7#Full sync (download changes)

python dropbox_sync.py sync --mirror "./mirror_algo2025" --report "./reports"


8#Create ZIP of updated files

python dropbox_sync.py zip-updates --mirror "./mirror_algo2025" --report "./reports" --out "./to_moodle.zip"



