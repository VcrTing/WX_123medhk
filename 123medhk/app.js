const HOST = 'http://127.0.0.1:8000'
const API = {
  'ORDER': {
    'MAIN': HOST + '/api/order/'
  },
  'MEMBER': {
    'LOGIN': HOST + '/api/member/login/'
  }
}
const APPID = '	wx1f12b464cfa49b00'
const SECRET = '24e18921aaa46b539a00ee0a7fc07ae8'

App({
  onLaunch: function () {
  },
  globalData: {
    userInfo: null,
    memberId: '',
    api: API,
    appId: APPID,
    secret: SECRET,
  },
  toast: function (msg, icon) {
    wx.showToast({
      title: msg,
      icon: icon,
      duration: 3000,
      mask: true
    })
  },
  save: function (name, value) {
    wx.setStorageSync(name, value)
  },
  read: function (name) {
    return wx.getStorageSync(name)
  },
  now: function (str, mode) {
    let now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth();
    const date = now.getDate();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    if (mode == 'date') {
      return year + str + month + str + date
    } else if (mode == 'time') {
      return hours + str + minutes + str + seconds
    } else if (mode == 'time_two') {
      return hours + str + minutes
    }
  }
})