# 샘플 이미지 생성 방법

`sample_dataset/images` 폴더에 포함된 샘플 이미지는 실제 데이터셋이 아니라  
테스트용으로 생성된 **placeholder 이미지**입니다.

이 프로젝트에서는 COCO 데이터셋 검증 로직을 테스트하기 위한 목적이기 때문에  
대용량 실제 이미지를 저장소에 포함시키지 않고 간단한 이미지를 생성해서 사용했습니다.

---

## 생성 방법

샘플 이미지는 `picsum.photos` placeholder 이미지 서비스를 이용해 다운로드했습니다.

예시 명령어:

```bash
curl -o image_001.jpg https://picsum.photos/640/480
curl -o image_002.jpg https://picsum.photos/640/480
curl -o image_003.jpg https://picsum.photos/640/480
curl -o image_004.jpg https://picsum.photos/640/480
curl -o image_005.jpg https://picsum.photos/640/480
````

이 명령은 640x480 크기의 랜덤 이미지를 다운로드합니다.

---

## 사용 목적

이 이미지들은 실제 학습 데이터가 아니라
COCO 데이터셋 구조를 테스트하기 위한 용도로만 사용됩니다.

샘플 데이터셋에는 일부 오류가 의도적으로 포함되어 있습니다.

예를 들어 다음과 같은 상황을 테스트합니다.

* 실제 파일이 존재하지 않는 이미지
* 존재하지 않는 image ID를 참조하는 annotation
* annotation이 없는 이미지

이러한 오류를 통해 데이터셋 검증 기능이 정상적으로 동작하는지 확인할 수 있습니다.

---

## 대체 방법 (오프라인 환경)

인터넷 연결이 없는 환경에서는 ImageMagick을 사용하여
placeholder 이미지를 직접 생성할 수도 있습니다.

예시:

```bash
convert -size 640x480 xc:gray image_001.jpg
convert -size 640x480 xc:gray image_002.jpg
```

이 명령은 640x480 크기의 단색 이미지를 생성합니다.
