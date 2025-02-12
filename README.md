# Test Backend BTSDotID
Test Teknikal Backend Interview BTS Dot ID(PT Intersolusi Teknologi Asia)

# Cara running web server dan Testing Api:

1. [Download Python](https://www.python.org/downloads/)
2. Install Python and then setting Environment variabel Path System: contoh path python C:\Python388\Scripts dan C:\Python388\ copy paste ke Env Var path system
3. Buat dan Aktifkan Virtual Machine Env ketik di cmd dalam root folder project: perintah cmd Buat Virtual Machine Env: python -m venv nama virtualmachine_env,perintah aktifkan virtual machine env cd nama_virtualmachine_env kemudian ketik cd Scripts dan setelah itu ketik activate.bat
4. Ketik cd .. untuk mengarahkan kembali ke path root project
5. Ketik cd .. untuk mengarahkan kembali ke path root project
6. Kemudian install library dengan ketik di cmd: pip install -r requirements.txt
7. Setelah itu keyik flask run untuk website running.
8. Web Server running on http://127.0.0.1:5000
9. Selesai.

# Cara Testing API:

1. Register User: curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"testing\", \"password\": \"testing123\"}" http://127.0.0.1:5000/register

2. Login User: curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"testing\", \"password\": \"testing123\"}" http://127.0.0.1:5000/login

3. Create Checklist: curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RpbmciLCJleHAiOjE3MzkzNTI3MTl9.3yX86P4bLtcR8KSsQajnNQNnfYSZn3DPc9DUAuqiFCg" -d "{\"title\": \"My Checklist\"}" http://127.0.0.1:5000/checklist

4. Create Item: curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RpbmciLCJleHAiOjE3MzkzNTI3MTl9.3yX86P4bLtcR8KSsQajnNQNnfYSZn3DPc9DUAuqiFCg" -d "{\"description\": \"My Item\"}" http://127.0.0.1:5000/checklist/1/item

5. Complete Item: curl -X PUT -H "Content-Type: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RpbmciLCJleHAiOjE3MzkzNTI3MTl9.3yX86P4bLtcR8KSsQajnNQNnfYSZn3DPc9DUAuqiFCg" http://127.0.0.1:5000/item/1/complete

6. Delete Item: curl -X DELETE -H "Content-Type: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RpbmciLCJleHAiOjE3MzkzNTI3MTl9.3yX86P4bLtcR8KSsQajnNQNnfYSZn3DPc9DUAuqiFCg" http://127.0.0.1:5000/item/1
