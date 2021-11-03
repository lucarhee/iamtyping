iamtyping
=========

타자 연습 프로그램

* github의 코드를 가지고 타자 연습할 수 있다.
* 프로그래밍 언어를 설정할 수 있다.
* repository를 설정할 수 있다.
* 보이는 코드 줄 수를 설정할 수 있다.
* 언어를 선택할 수 있다.
* 언어에 따라 최근 기사나 위키글을 가지고 타자 연습을 할 수 있다. - web scraping
* 사이트에서 자신의 위치를 확인할 수 있다.
* 자판 설정을 할 수 있다.
* 사용자 입력
* 연습한 양과 시간과 속도를 기록
* 표로 보여준다.
* 그래프로 보여준다.

----

타이핑 속도는 어떻게 계산할 것인가?

타이핑 수 / 지난 시간
시간은 키스트로크가 있을 때마다 총시간을 계산한다.
전체 문장이 다 끝나고 엔터를 치면 그 시간 계산은 끝난다.

마이크로 시간을 구할 필요가 있다.
마이크로 시간을 얻는 방법은?

::

   from datetime import datetime

   time1 = datetime.now()
   time2 = datetime.now()
   timedelta = time2 - time1

   # seconds + microseconds
   print(timedelta.totalseconds())

타이핑 계산을 위해서 순환문을 두 개 써야 한다.
하나는 ctrl+c를 누를 때까지 계속 하고,
하나는 엔터를 치면 종료되는 것으로.
