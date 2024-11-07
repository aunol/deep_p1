from Korpora import Korpora

# 감성 분석 데이터 다운로드
Korpora.fetch("nsmc", root_dir="data/korean")

# 네이버 영화 리뷰 감성 데이터가 `~/.korpora` 폴더에 다운로드됩니다.