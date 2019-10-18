//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    record: [],
    memberId: '',
    r_num: '',
    userInfo: {},
    hasUserInfo: false,

    sex: 'female',
    name: '',
    phone: '',
    birth: '1999-1-1',
    reserve_date: '',
    reserve_time: '',
    start_time: '6:00',
    end_time: '23:00'

  },
  _load_nowifi: function () {
    const record = require("../../../utils/data.js").record
    this.setData({
      record: record
    })
    app.save('record', record)
  },
  //事件处理函数
  onReady: function () {

  },
  onLoad: function () {
    const date = app.now('-', 'date')
    const time = app.now(':', 'time_two')
    this.setData({
      reserve_date: date,
      reserve_time: time
    })
  },
  onShow: function () {
    const is_login = app.globalData.memberId
    if (!is_login) {
      app.toast('未授权，预约表单需授权后才可提交！！！', 'none')
    }
  },
  //表单
  submit: function () {
    const is_name = this._valide_name(this)
    const is_phone = this._valide_phone(this)
    const is_login = app.globalData.memberId
    if (!is_login) {
      app.toast('未授权，请在首页进行授权，成功后再次提交表单！！！', 'none')
      return
    }
    if (is_name != true) {
      app.toast(is_name, 'none')
      return
    }
    if (is_phone != true) {
      this._msg(is_phone)
      return
    }
    this._submit()
  },
  _submit: function () {
    const self = this
    const memberId = app.globalData.memberId
    const data = {
      'name': this.data.name,
      'sex': this.data.sex,
      'birth': this.data.birth,
      'phone': this.data.phone,
      'reserve_date': this.data.reserve_date,
      'reserve_time': this.data.reserve_time,
      'member': memberId
    }
    wx.request({
      url: app.globalData.api.ORDER.MAIN,
      method: 'POST',
      data: JSON.stringify(data),
      success: (res) => {
        const navUrl = '/pages/Book/record/add_success/add_success?reserve_time=' + this.data.reserve_time + '&name=' + this.data.name + '&reserve_date=' + this.data.reserve_date
        wx.redirectTo({
          url: navUrl
        })
      },
      fail: (err) => {
        app.toast('請檢查網絡連接!!!', 'loading')
        // self._submit_nowifi(data)
      }
    })
  },
  _submit_nowifi: function (data) {
    data['status'] = true
    data['is_complete'] = 1
    data['id'] = app.now('', 'date') + '' + Math.random() * 100
    let record = app.read('record')
    try {
      record.unshift(data)
    } catch (e) {
      record = []
      record.push(data)
    }
    app.save('record', record)
    const navUrl = '/pages/Book/record/add_success/add_success?reserve_time=' + this.data.reserve_time + '&name=' + this.data.name + '&reserve_date=' + this.data.reserve_date
    wx.redirectTo({
      url: navUrl
    })
  },
  formName: function (e) {
    this.setData({
      name: e.detail.value
    })
    console.log('1')
  },
  formBirth: function (e) {
    this.setData({
      birth: e.detail.value
    })
    console.log('2')
  },
  formSex: function (e) {
    this.setData({
      sex: e.detail.value
    })
    console.log('3')
  },
  formPhone: function (e) {
    this.setData({
      phone: e.detail.value
    })
    console.log('4')
  },
  formDate: function (e) {
    this.setData({
      reserve_date: e.detail.value
    })
    console.log('5')
  },
  formTime: function (e) {
    this.setData({
      reserve_time: e.detail.value
    })
    console.log('6')
  },
  _msg: function (is_msg) {
    /*
    wx.showModal({
      title: '提示',
      content: is_msg
    })
    */
    app.toast(is_msg, 'none')
  },
  _valide_name(self) {
    const name = self.data.name
    if (!name | name == undefined) {
      return '請檢查輸入！！！'
    } else {
      const len = name.length
      const char = /[`~!@#$%^&*()+-<>?:"{},.\/;'[\]]/;
      if (len < 2) {
        return '請確保名字的字數大於2。'
      } else if (len > 60) {
        return '請確保名字的字數小於60。'
      }
      if (!isNaN(name)) {
        return '請確保名字中不出現數字！！！'
      }
      if (char.test(name)) {
        return '請檢查姓名的正確性！！！'
      }
    }
    return true
  },
  _valide_phone(self) {
    const phone = self.data.phone
    if (!phone | phone == undefined) {
      //
    } else {
      const len = phone.length
      const char = /[`~!@#$%^&*()+<>?:"{},.\/;'[\]]/;
      if (len < 2) {
        return '請確保號碼的字數大於2。'
      } else if (len > 60) {
        return '請確保號碼的字數小於60。'
      }
      if (char.test(phone)) {
        return '名字裏不需要特殊字符！！！'
      }
    }
    return true
  }
})
