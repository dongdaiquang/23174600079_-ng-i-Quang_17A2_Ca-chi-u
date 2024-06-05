import time
import csv
def tao_so_ngau_nhien():
    current_time=time.time()
    return int((current_time*1000)%100)+1
def rut_so(danh_sach,so_rut=1):
    for _ in range(so_rut):
        number=tao_so_ngau_nhien()
        danh_sach.append(number)
        time.sleep(0.001)
    return danh_sach
def kiem_tra_ket_qua(danh_sach,guess_set):
    hit=guess_set.intersection(danh_sach)
    return hit
def tinh_xac_suat(danh_sach):
    xac_suat={i: 0 for i in range(1,101)}
    tong=len(danh_sach)
    for number in danh_sach:
        xac_suat[number]+=1
    for number in xac_suat:
        xac_suat[number]/=tong
    return xac_suat
def tien_thuong(hit):
    prize_per_hit=1000
    return len(hit)*prize_per_hit
def main():
    results=[]
    so_nguoi_choi=5
    nhap_so=int(input("nhap so lan doan"))
    for game_number in range(1, so_nguoi_choi+1):
        danh_sach=[]
        guess_set={tao_so_ngau_nhien() for _ in range(nhap_so)}
        so_rut=1000
        rut_so(danh_sach,so_rut)
        hit=kiem_tra_ket_qua(danh_sach,guess_set)
        probabilities=tinh_xac_suat(danh_sach)
        prize=tien_thuong(hit)
        results.append({
            'game': game_number,
            'guess_set': list(guess_set),
            'hit': list(hit),
            'prize': prize,
            'probabilities': probabilities
        })
        print(f"Game {game_number}")
        print(f"Guess Set: {guess_set}")
        print(f"Hit:{hit}")
        print(f"Prize: {prize}")
        print(f"Probabilities: {probabilities}")
        print("-" * 40)
        with open('lottery_resulis.csv', mode='w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['Game', 'Guess Set', 'Hit', 'Prize', 'Probabilities'])
            for result in results:
                writer.writerow([result['game'], result['guess_set'], result['hit'], result['prize'], result['probabilities']])
if __name__ == "__main__":
    main()
    
