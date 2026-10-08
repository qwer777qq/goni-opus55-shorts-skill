# 고니 Claude 숏폼 제작 스킬

Claude Opus 5.5와 Codex에서 제품 모션그래픽·세로형 숏폼을 제작할 때 쓰는 고니 수강생용 스킬입니다. [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)의 프롬프트 목록을 검색 가능한 참고 자료로 정리하고, 상품 사진 기반 영상 제작·TTS·자막·출력 검수 절차를 추가했습니다.

**수강생 시작점:** [설치와 복사용 프롬프트](STUDENT_START.md) → [실제 제작 사례](docs/claude-shorts-guide.md)

## 들어 있는 것

- `SKILL.md`: 레퍼런스 선택부터 최종 영상 검수까지의 작업 절차
- `references/videos.json`: 원본 저장소의 영상·프롬프트 513개를 정리한 카탈로그
- `scripts/find_references.py`: 카테고리·태그·검색어로 참고 사례 찾기
- `docs/claude-shorts-guide.md`: 실제 ESR 제품 광고 제작 사례와 Claude에 보낸 지시문

## 설치

이 저장소를 내려받아 폴더를 `opus55-motion-graphics`라는 이름으로 복사합니다.

```bash
git clone https://github.com/qwer777qq/goni-opus55-shorts-skill.git
```

- Codex: `~/.codex/skills/opus55-motion-graphics`
- Claude Code: `~/.claude/skills/opus55-motion-graphics`

Claude 웹에서 Git/파일 도구가 없으면 [Claude Skills 업로드용 ZIP](https://github.com/qwer777qq/goni-opus55-shorts-skill/releases/latest/download/goni-opus55-shorts-skill-claude-upload.zip)을 내려받아 **Customize → Skills**에서 업로드합니다. ZIP의 최상위에 `SKILL.md`, `references/`, `scripts/`가 있습니다. 설치 위치와 메뉴는 사용 중인 앱 버전에 따라 다를 수 있습니다.

## 레퍼런스 검색

```bash
python scripts/find_references.py "product reveal" --category motion --limit 8
```

검색 결과에서 원본 영상·프롬프트를 확인하고, 제품에 맞는 전환·타이포·카메라 움직임만 골라 응용합니다. 이 카탈로그는 모든 영상의 완성 소스 코드를 포함하지 않습니다.

## 제작 사례

[Claude로 숏폼 만드는 방법](docs/claude-shorts-guide.md)에 실제로 보낸 첫 요청과 렌더 수정 요청, 20초 구성표, 복사용 프롬프트를 담았습니다. 사례의 최종 영상은 1080×1920, 30fps, 20초 MP4였습니다. 상업 게시 전에는 상품 사진의 사용 권리와 광고 문구를 별도로 확인해야 합니다.

## 원본과 라이선스

레퍼런스 데이터의 원본은 [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos), 스냅샷 커밋은 `756290289742535eb0ac3817548f152e9759cc70`입니다. 원본의 MIT 라이선스 전문은 [`references/LICENSE`](references/LICENSE)에 보존했습니다. 원본 레퍼런스·영상·프롬프트의 창작자는 각 항목에 표시된 저작자입니다. 이 저장소의 새 기여는 스킬 절차, 검색 스크립트, 한국어 제작 가이드입니다.
