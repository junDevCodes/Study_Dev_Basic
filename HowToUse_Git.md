# How to use Git

## git init
- 깃 초기화

## git add
- 변경사항이 있는 파일을 staging area로 추가
- ex) git add . (전체 파일 추가) / git add 파일명 (특정 파일 추가)

## git commit
- staging area에 있는 파일들을 repository에 기록
- ex) git commit -m "commit msg" (-m "커밋 메세지"를 통해 기록 남기기 가능)

## git status
- working area, staging area의 상태 표시

## git log
- repository에 기록된 log 불러오기

## git flow
[![image.png](https://i.postimg.cc/J7gFDGDS/image.png)](https://postimg.cc/Z08HXYLL)

## 사용자 설정
- git config --global user.email "메일 주소"
- git config --global user.name "유저 네임"

## git config --global alias.(단축어) 명령
- 원하는 명령을 단축키 생성 가능
- ex) git config --global alias.st status
- git st == git status
