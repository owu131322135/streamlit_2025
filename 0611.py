import streamlit as st
import random

# 都道府県と観光名所の辞書
prefecture_spots = {
    "北海道": ["富良野のラベンダー畑", "小樽運河", "札幌時計台"],
    "京都府": ["金閣寺", "清水寺", "嵐山"],
    "沖縄県": ["美ら海水族館", "首里城", "国際通り"],
    "東京都": ["東京スカイツリー", "浅草寺", "上野動物園"],
    "広島県": ["厳島神社", "原爆ドーム", "宮島水族館"],
    "長野県": ["善光寺", "上高地", "松本城"],
    "福岡県": ["大濠公園", "博多ラーメン屋台", "太宰府天満宮"]
    # 必要に応じて追加できます
}

# 都道府県リストを辞書のキーから取得
prefectures = list(prefecture_spots.keys())

st.title("🎲 ランダム都道府県＆観光スポットガチャ")

if st.button("都道府県を引く！"):
    selected = random.choice(prefectures)
    spots = prefecture_spots[selected]

    st.success(f"🎉 あなたの行き先は：**{selected}**")
    st.subheader("🏞️ おすすめ観光スポット")
    for spot in spots:
        st.markdown(f"- {spot}")
else:
    st.info("ボタンを押すと、ランダムな都道府県と観光名所が表示されます。")
