/*
const is_email = this._valide_email(this)
const is_mark = this._valide_mark(this)
const is_contry = this._valide_contry(this)

if (is_contry != true) {
  this._msg(is_contry)
  return
}
if (is_email != true) {
  this._msg(is_email)
  return
}
if (is_mark != true) {
  this._msg(is_mark)
  return
}

formMark: function (e) {
  this.setData({
    mark: e.detail.value
  })
  console.log('7')
},
formEmail: function (e) {
  this.setData({
    email: e.detail.value
  })
  console.log('5')
},
formContry: function (e) {
  this.setData({
    contry: e.detail.value
  })
  console.log('4')
},


_valide_email() {
  const email = this.data.email;
  const char = /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
  if (!char.test(email)) {
    return '請確保郵箱格式正確！！！'
  }
  return true
},
_valide_contry() {
  const contry = this.data.contry
  if (!contry | contry == undefined) {
    return '國籍必填！！！'
  } else {
    const len = contry.length
    if (len < 2) {
      return '國籍的字數應該大於2。'
    } else if (len > 90) {
      return '國籍的字數應該小於90。'
    }
  }
  return true
},
_valide_mark() {
  const mark = this.data.mark
  if (!mark | mark == undefined) {
    return '請讓我們了解到妳的癥狀。'
  } else {
    const len = mark.length
    if (len < 8) {
      return '癥狀的字數應該大於8。'
    } else if (len > 240) {
      return '癥狀的字數應該小於240。'
    }
  }
  return true
}
*/