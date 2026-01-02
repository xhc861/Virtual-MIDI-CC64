import mido
import time

# 获
# LoopMIDI First
loopmidi_port_name = None
for name in output_names:
    if "loopmidi

if loopmidi_port_name is None:
    print("LoopMIDI port not found. Please make sure LoopMIDI is running and a port is created.")
    exit(1)

print(f"Connecting to: {loopmidi_port_name}")

# 打开 MIDI 输出端口
with mido.open_output(loopmidi_port_name) as port:
    print("Connected. Starting MIDI loop...")
    try:
        while True:
            # 发送 CC64, value=127 (Sustain On)
            msg_on = mido.Message('control_change', control=64, value=127)
            port.send(msg_on)
            print(f"Sent: {msg_on} at {time.time()}")
            
            # 等待 2 秒
            time.sleep(2)
            
            # 发送 CC64, value=0 (Sustain Off) [[3]]
            msg_off = mido.Message('control_change', control=64, value=0)
            port.send(msg_off)
            print(f"Sent: {msg_off} at {time.time()}")
            
            # 等待 3 秒，完成 5 秒周期
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("Stopping...")
