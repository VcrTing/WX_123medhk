//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    record: [],
    memberId: '',
    r_num: '',
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),

    swiperUrl: [{
      "url": "https://tech.up5d.com/wp-content/uploads/2016/06/bg1.jpg"
    }, {
      "url": "https://tech.up5d.com/wp-content/uploads/2016/06/bg3.jpg"
    }],

    fade: '',
    slide: '',
    show_modal: false
  },
  //事件处理函数
  modalOut: function () {
    this.fade.opacity(0).step()
    this.slide.translateY(-120).step()

    this.setData({
      fade: this.fade.export(),
      slide: this.slide.export()
    })
    setTimeout(() => {
      this.setData({
        show_modal: false
      })
    }, 3000)
  },
  goRecord: function () {
    wx.switchTab({
      url: '/pages/Book/record/add/add',
    })
  },
  onReady: function () {
    this.fade = wx.createAnimation({
      duration: 2000,
      timingFunction: 'ease',
      delay: 300
    })
    this.slide = wx.createAnimation({
      duration: 2000,
      timingFunction: 'ease',
      delay: 300
    })
  },
  onLoad: function () {
    /*
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        },
        fail: res => {
        }
      })
    }
    */
  },
  onShow: function () {
    this.member()
  },
  _member: function (res) {
    const self = this
    this.setData({
      userInfo: res
    })
    wx.login({
      success: function (res) {
        const code = res.code
        const url = app.globalData.api.MEMBER.LOGIN
        wx.request({
          url: url,
          method: 'POST',
          data: JSON.stringify({
            code: code,
            appid: app.globalData.appId,
            secret: app.globalData.secret,
            userInfo: self.data.userInfo
          }),
          success: (res) => {
            res = res.data
            self.setData({
              memberId: res.id,
              r_num: res.openid
            })
            app.globalData.memberId = res.id
            console.log('memberid =', res.id)
          },
          fail: (err) => {
            console.log('member Error: ', err)
          }
        })
      }
    })
  },
  member: function () {
    wx.getUserInfo({
      success: (res) => {
        this.modalOut()
        res = res.userInfo
        this._member(res)
      },
      fail: (err) => {
        console.log('应该授权！！')
        this.setData({
          show_modal: true
        })
      }
    })
  },
  getUserInfo: function (e) {
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
    this.member()
  },
  _msg: function (is_msg) {
    /*
    wx.showModal({
      title: '提示',
      content: is_msg
    })
    */
    app.toast(is_msg, 'none')
  }
})
