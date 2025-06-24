import dropbox
import json
import os
from datetime import datetime

ACCESS_TOKEN = 'sl.u.AFwoAHSi_PnABpqu9CpCaPb6k2ZAjr8b02MsCeK-iaQcSXqDK3qakagjCNdiB8vu_7w-wdsLyV5c2NHNcaLXq085PsCpFzCRrV4mFGSqI8FQszrbsLoQYDciRJgVKOJg01it5yOnms2WrSchKSdBQcUWT-fvWEzY_1s31APOHTNLKU1DsFtv692fpfXDxYLLD_Rzvwi94Mv42KmDsve715v1L6t3_ubabii9MOf3M3FjpFX7rdTF5-adxIUtXWxh1yDvm7IjYQgonoFTvCa0Nlug5Awyf5WEqX_Cc-HsZjwRBNPXfdf4fWI73DACKT3yUBsMNOsTTLjhtXFLvHttq6dl41DomuHYq1amJ0zxztYU3kUGv0HlNM5XCKN73PbN--E8mWytsFMREs4s31-2LvAvyz748nBKkUjB2XlJbgqKveP3e9x4H_Ij654ZZA5AHZGe1YkJK5IPZLAu2Wi2gVaAuySOI-_FN3SMk2DsWnKw8nnQ-J6zAb1z5ykQ5laLRxsv9W4pOgvbDMYObjm1KbR4rgqPR2WOjnN3f59mUVfUbDo-vYjRhtXaygBrYxQukyoZAJA1qYRufvDGqc8bul3HgqFjdux5PRILypArQBsTp4Z8ln31zDrlYh4UhIcGWqEVw5ptv3jOT4nEtDSdrKhwKULZ8Vr9y8iPnqG-b82if0RXZ5POW-4zwcFUHuhuvNF0OPrar4w9wrX68zs95kcA6v0TwxVVlMf71QS4Eujr5qCoTv00FjqvAmD1bqhz8TVDj9_7uVL58kcz_byS-KSYArPSG2rilCmT0X7mDeZzQTqZ2gzX4teFMFDABVos1FJGSNksakp8gE0yaO0w1eljw0Ya7YKp5R16_W5qqKP6Dbt3FEmmNCknE8Vrxm128ry-KKyRSpeInnOjQWSU1IExjQxAFKsGtJiVknqHeES9xyl4EHeo2JShRs8U1QkXG5CRDDe2eWvJcHzJ5aSjMXnSDCq6zrJ_6lHQrnM80A3rhx63wQl4eQvvMFcvfOIZYEEhz7sbGCrnkeSbPpAUVLIqMnW35JIV18QR-e-GK-trXaRRc0sdhK6mEzFJ5RoH4snBaqHT91kH7UzI5OgA7d4X82DQa-rAUaKNuuI_6lhq1GLNS2I22gK0A1CVifiBm9VqaxxKfuZTEcvM-zYuo1CJyfpezbouJHb7zemuYFbk6D9ZRB3O8Sa2A4IdL-VVnH686fg9REQzgUfd4uuBu-vTxnYAUxwrkpNZjkPITi6WgV7lfttHEhm3NyQKSqEHCXCKfAg6pfUZUXO1kA0qxxvzItCJne9w0iCGt7xQ4gFgmW9Wbgz1hGVppFJVBCQprx0dOiqraTeClUo9x7ykU1qoz6yHij_3oto8zGE4dBVuQhNaGdLLl5Wj12FzN_OY1UBOHEalnbLlBbUpQJodI3XRtp363AZRWJmHcAtBCjJhJExSU3-U5j3HzZjrPzG5p3Q'  # ← הדבק כאן את הטוקן שלך
dropbox_path = '/example.pdf'
local_path = 'downloaded_example.pdf'
timestamp_file = 'last_modified.json'

dbx = dropbox.Dropbox(ACCESS_TOKEN)

# קבלת זמן השינוי מהקובץ ב-Dropbox
metadata = dbx.files_get_metadata(dropbox_path)
current_modified = metadata.client_modified.isoformat()
print("📅 Last modified:", current_modified)

# בדיקה אם יש קובץ עם זמן קודם
last_modified = None
if os.path.exists(timestamp_file):
    with open(timestamp_file, 'r') as f:
        data = json.load(f)
        last_modified = data.get('modified')

# השוואה וזיהוי שינוי
if last_modified == current_modified:
    print("⚠️ No changes detected, skipping download.")
else:
    print("⬇️ Change detected, downloading file...")
    with open(local_path, "wb") as f:
        _, res = dbx.files_download(path=dropbox_path)
        f.write(res.content)
    print("✅ File downloaded successfully!")

    # עדכון קובץ הזמן
    with open(timestamp_file, 'w') as f:
        json.dump({'modified': current_modified}, f)