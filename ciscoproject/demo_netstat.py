import paramiko, pandas as pd
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.0.2.15",username="afrin",password="afrin")
stdin,stdout,stderr,=ssh.exec_command("netstat --listening|less")
df=pd.DataFrame(stdout)

print(df)