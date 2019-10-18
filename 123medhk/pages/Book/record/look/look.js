
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    id: 0,
    record: { }
  },
  goBack: function () {
    wx.navigateBack({
      param: 1,
    })
  },
  trash: function (e) {
    const self = this
    const url = app.globalData.api.ORDER.MAIN + self.data.id + '/'
    wx.showModal({
      title: '提示',
      content: '確定要刪除嗎？',
      success: function (res) {
        if (res.confirm) {
          wx.request({
            url: url,
            method: 'PUT',
            data: JSON.stringify({
              status: false
            }),
            success: (res) => {
              app.toast('刪除成功!!!', 'success')
              setTimeout(() => {
                wx.switchTab({
                  url: '/pages/Book/record/record'
                })
              }, 2000)
            },
            fail: (err) => {
              app.toast('網絡錯誤！刪除失敗！！！', 'none')
              // self._trash_nowifi()
            }
          })
        }
      }
    })
  },
  recordLook: function (id) {
    const self = this
    const url = app.globalData.api.ORDER.MAIN + id + '/'
    wx.request({
      url: url,
      method: 'GET',
      success: (res) => {
        this.setData({
          record: res.data
        })
      },
      fail: (err) => {
        const record = app.read('record')
        for (var i = 0; i < record.length; i++) {
          const res = record[i]
          if (res.id == id) {
            self.setData({
              record: res
            })
          }
        }
      }
    })
  },
  _trash_nowifi: function () {
    let record = app.read('record')
    for (var i = 0; i < record.length; i++) {
      const res = record[i]
      if (res.id == this.data.id) {
        record.splice(i, 1)
      }
    }
    app.save('record', record)
    app.toast('刪除成功!!!', 'success')
    setTimeout(() => {
      wx.switchTab({
        url: '/pages/Book/record/record'
      })
    }, 2000)
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const id = options.id
    this.recordLook(id)
    this.setData({
      id: id
    })
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