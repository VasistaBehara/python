def parse_logs(logs):
    parsed_logs = []
    status_dict = {
        'total': 0,
        'valid': 0,
        'invalid': 0,
        'status_count': {},
        'top_ip': ""
    }
    for log in logs:
        log_dict = {}
        status_dict['total'] += 1
        parts = log.split()
        for part in parts:
            if '=' in part:
                key, value = part.split('=', 1)
                log_dict[key] = value
        # Validate required fields
        if 'ip' not in log_dict or (not log_dict['status'].isdigit() and 100 < log_dict['status'] > 599) or 'user' not in log_dict:
            status_dict['invalid'] += 1
        else:
            status_dict['valid'] += 1
            status_code = log_dict['status']
            status_dict['status_count'][status_code] = status_dict['status_count'].get(status_code, 0) + 1
        parsed_logs.append(log_dict)
    print(parsed_logs)

logs = [
  "INFO user=admin ip=10.0.0.5 status=200",
  "WARN user=test ip=192.168.1.10 status=500",
  "ERROR user=guest ip=172.16.0.1 status=403",
  "INFO user=admin status=200",                 # missing ip
  "WARN ip=10.0.0.5 status=ABC user=admin",     # invalid status
]
parse_logs(logs)