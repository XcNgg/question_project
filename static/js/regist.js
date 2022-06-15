// 在jquery 当中 $()里的代码都是会等待网页文档加载完毕后才会执行
$(function () {
        bindCaptchaBtnClick();
    }
)


function bindCaptchaBtnClick() {
    // 通过# 寻找ID 绑定按钮
    // 点击事件
    $('#email-captcha-btn').on('click', function (event) {
            //jquery this 封装 $('#email-captcha-btn')
            var $this = $(this);

            var email = $('input[name="email"]').val();
            if (!email) {
                alert("请输入邮箱！");
                return
            } else {
                // var jq = jQuery.noConflict();
                //通过js发送请求，Ajax;Async JavaScript JSON
                $.ajax({
                    url: "/users/email",
                    //请求方法
                    method: "POST",
                    //提交表单
                    data: {
                        "email": email,
                    },
                    //
                    success: function (res) {
                        var code = res['code'];
                        if (code == 200) {
                            //锁定获取验证码
                            $this.off('click')
                            //设置倒计时
                            var countDown = 60;
                            var timer = setInterval(function () {
                                 countDown -=1;
                                if (countDown > 0) {
                                 $this.text(countDown + "秒后可重新获取");
                                }
                                else{
                                    $this.text( "获取验证码");
                                    // 重新执行下这个函数，重新绑定点击事件
                                    bindCaptchaBtnClick();
                                    // 如果不需要倒计时，那么就要记得清除倒计时，否则会一直执行下去
                                    clearInterval(timer);
                                }
                            },1000)
                            alert("验证码发送成功!");
                        } else {
                            alert(res['message']);
                        }
                    }
                })
            }
        }
    )


}

