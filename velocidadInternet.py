import speedtest
st = speedtest.Speedtest()
print(st.download()/1024)
print(st.upload()/1024)
