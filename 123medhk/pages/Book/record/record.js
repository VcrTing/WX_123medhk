const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    record: [ ],
    is_null: false
  },
  record: function () {
    const self = this
    const url = app.globalData.api.ORDER.MAIN + '?status=true&ordering=-id'
    wx.request({
      url: url,
      method: 'GET',
      success: (res) => {
        res = res.data
        if (res.length >= 1) {
          this.setData({
            record: res,
            is_null: false
          })
          app.save('record', res)
        } else {
          this.setData({
            is_null: true
          })
        }
        console.log(res, self.data.is_null)
      },
      fail: (err) => {
        const res = app.read('record')
        console.log('record res =', res.length)
        if (res.length >= 1) {
          this.setData({
            record: res,
            is_null: false
          })
        } else {
          this.setData({
            is_null: true
          })
        }
        console.log('record data =', this.data.record)
      }
    })
  },
  recordLook: function (e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: '/pages/Book/record/look/look?id='+ id
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    const is_login = app.globalData.memberId
    if (is_login) {
      this.record()
    } else {
      app.toast('未授权，无法查看预约记录！！！', 'none')
    }
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})