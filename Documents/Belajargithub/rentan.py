import sqlite3

def buat_database():
    # Membuat basis data sementara di memori
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Membuat tabel pengguna dan menambahkan data sampel
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'SuperSecret123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password123')")
    conn.commit()
    return conn

def login_rentan(conn, username, password):
    cursor = conn.cursor()
    
    # PERHATIAN: Baris ini RENTAN terhadap SQL Injection!
    # Input pengguna digabungkan langsung ke dalam string query SQL.
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"\n[DEBUG] Query SQL yang dijalankan:\n{query}\n")
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        
        if user:
            print(f"[SUCCESS] Login Berhasil! Selamat datang, {user[1]}.")
        else:
            print("[FAILED] Login Gagal! Username atau password salah.")
    except sqlite3.OperationalError as e:
        print(f"[ERROR] Query SQL Rusak/Gagal: {e}")

if __name__ == "__main__":
    conn = buat_database()
    
    print("=== DEMO APLIKASI RENTAN SQL INJECTION ===")
    user_input = input("Masukkan Username: ")
    pass_input = input("Masukkan Password: ")
    
    login_rentan(conn, user_input, pass_input)
    conn.close()