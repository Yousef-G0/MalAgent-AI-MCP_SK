import os
from datetime import datetime

def run(params):
    report_content = params.get("report", "")
    report_name = params.get("name", "")

    if not report_content or not report_name:
        return {"error": "Missing 'report' or 'name' parameter."}

    # Ensure report directory exists
    output_dir = "uploaded_reports"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{report_name}_{timestamp}.md"
    file_path = os.path.join(output_dir, filename)

    with open(file_path, "w") as f:
        f.write(report_content)

    return {
        "status": "success",
        "saved_path": file_path
    }
