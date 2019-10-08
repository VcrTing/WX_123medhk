// pages/Book/record/add_success/add_success.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name: '',
    reserve_time: '',
    reserve_date: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const name = options.name
    const reserve_time = options.reserve_time
    const reserve_date = options.reserve_date
    this.setData({
      name: name,
      reserve_time: reserve_time,
      reserve_date: reserve_date
    })
  },
  sure: function () {
    wx.switchTab({
      url: '/pages/Book/record/record'
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