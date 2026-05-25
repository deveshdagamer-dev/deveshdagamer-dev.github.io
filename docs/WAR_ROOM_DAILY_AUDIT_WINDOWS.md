# Website War Room Daily Audit On Windows

These instructions keep the Website War Room design unchanged. The automation
only refreshes the local audit report/data files used by the dashboard.

## 1. Install Dependencies

From the repository root:

```powershell
cd C:\Users\deves\OneDrive\Desktop\deveshdagamer-dev.github.io
npm install
```

## 2. Run The Audit Manually

To run the same audit used by the dashboard:

```powershell
npm run audit:site
```

To run the daily wrapper manually, including the War Room state file:

```powershell
npm run audit:daily
```

Both commands refresh:

```text
reports/latest-website-audit.md
```

The daily wrapper also refreshes:

```text
reports/war-room-audit-state.json
```

The dashboard's `Last audit time` comes from the `Generated:` timestamp in
`reports/latest-website-audit.md`.

## 3. Schedule It Daily With Windows Task Scheduler

1. Open **Task Scheduler**.
2. Choose **Create Basic Task...**.
3. Name it `Website War Room Daily Audit`.
4. Choose **Daily** and select the preferred time.
5. For **Action**, choose **Start a program**.
6. In **Program/script**, enter:

```text
npm
```

7. In **Add arguments**, enter:

```text
run audit:daily
```

8. In **Start in**, enter:

```text
C:\Users\deves\OneDrive\Desktop\deveshdagamer-dev.github.io
```

9. Finish the wizard.
10. Right-click the task and choose **Run** once to confirm it refreshes the report.

If Task Scheduler cannot find `npm`, use the full path shown by:

```powershell
where npm
```

## 4. Open The War Room Locally

Serve the repository root:

```powershell
cd C:\Users\deves\OneDrive\Desktop\deveshdagamer-dev.github.io
python -m http.server 8080
```

Then open:

```text
http://localhost:8080/tools/dashboard/war-room.html
```

## 5. Keep The Dashboard Design Unchanged

- Do not edit `tools/dashboard/war-room.html` for scheduling.
- Do not edit `tools/dashboard/war-room.css` for scheduling.
- Do not edit `tools/dashboard/war-room.js` unless the dashboard data format intentionally changes.
- Use `tools/audit/check-site.mjs` and `tools/audit/run-daily-audit.mjs` for automation changes.
