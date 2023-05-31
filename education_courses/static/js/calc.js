const packageInputs = document.querySelectorAll('input[name="package"]');
const tempInputs = document.querySelectorAll('input[name="temp"]');
const packageTitle = document.getElementById('packageTitle');
const packageSelect = document.getElementById('packageLevel');
const packageTime = document.getElementById('packageTime');
const packageWork = document.getElementById('packageWork');
const packageDiplom = document.getElementById('packageDiplom');
const programInput = document.getElementById('programInput');
const specialItem = document.getElementById('specialItem');
const individEducation = document.getElementById('individEducation');
const packageNames = document.querySelectorAll('.package__block h1');

const tempNames = document.querySelectorAll('.temp__block h1');
const tempTitle = document.getElementById('tempName');

const optionCheckbox = document.querySelector('input[name="option"]');

let selectedTempPriceIdInput;
let selectedPackagePriceIdInput;
const selectedCheckboxes = [];


// Получение ссылок на элементы
const checkboxes = document.querySelectorAll('.options__event input[type="checkbox"]');
const orderList = document.querySelector('.order__list .order__block');

checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      // Получение ссылок на элементы "h1" и "span" из соответствующего блока "option__selected"
      const optionRow = this.parentNode.querySelector('.option__selected');
      const optionName = optionRow.querySelector('h1');
      const optionPrice = optionRow.querySelector('.option__cost');
  
      // Проверка, выбран ли чекбокс
      if (this.checked) {
        // Создание нового элемента order__item
        const orderItem = document.createElement('div');
        orderItem.classList.add('order__item');
  
        // Создание элементов span
        const span1 = document.createElement('span');
        span1.textContent = optionName.textContent;
  
        const span2 = document.createElement('span');
        span2.id = `packageSelect_${this.value}`;
        span2.textContent = optionPrice.textContent;
  
        // Добавление элементов span в элемент order__item
        orderItem.appendChild(span1);
        orderItem.appendChild(span2);
  
        // Добавление элемента order__item в orderList
        orderList.appendChild(orderItem);
  
        // Добавляем выбранный чекбокс в массив выбранных чекбоксов
        selectedCheckboxes.push(this);
  
        // Передаем выбранные чекбоксы в функцию updateTotalValue
        updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput, selectedCheckboxes);
      } else {
        // Поиск и удаление элемента order__item с соответствующим id
        const orderItemToRemove = document.getElementById(`packageSelect_${this.value}`).closest('.order__item');
        orderItemToRemove.remove();
  
        // Удаляем отмененный чекбокс из массива выбранных чекбоксов
        const checkboxIndex = selectedCheckboxes.indexOf(this);
        if (checkboxIndex > -1) {
          selectedCheckboxes.splice(checkboxIndex, 1);
        }
  
        // Передаем обновленный массив выбранных чекбоксов в функцию updateTotalValue
        updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput, selectedCheckboxes);
      }
    });
  });


tempInputs.forEach(function(input) {
    input.addEventListener('change', function() {
        // Находим выбранный пакет
        const selectedTemp = Array.from(tempNames).find(tempName => tempName.textContent === this.parentNode.querySelector('h1').textContent);

        // Проверяем, найден ли пакет
        if (selectedTemp) {
            // Подставляем значение в атрибут id у элемента с идентификатором "packageTitle"
            tempTitle.textContent = selectedTemp.textContent;
            
            // Получаем значение атрибута data-package-id
            const tempId = this.getAttribute('data-temp-id');
            
            // Создаем соответствующие идентификаторы
            // const selectedPackageLevelId = `packageLevelInput_${packageId}`;
            // const selectedPackageTimeId = `packageTime_${packageId}`;
            // const selectedPackageWorkId = `packageWorking_${packageId}`;
            const selectedTempPriceId = `priceTemp_${tempId}`;

            console.log(selectedTempPriceId);
            
            // // Находим соответствующие элементы по их уникальным идентификаторам
            // const selectedPackageLevelInput = document.getElementById(selectedPackageLevelId);
            selectedTempPriceIdInput = document.getElementById(selectedTempPriceId);
            // const selectedPackageWorkingIdInput = document.getElementById(selectedPackageWorkId);
            // const selectedPackageDiplomIdInput = document.getElementById(selectedPackageDiplomId);

            console.log(selectedTempPriceIdInput);
            
            updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput, selectedCheckboxes);

            // // Проверяем, найдены ли элементы
            // if (selectedPackageLevelInput) {
            //     // Подставляем значения в соответствующие элементы
            //     packageSelect.textContent = selectedPackageLevelInput.textContent;
            // }

            // if (selectedPackageLevelInput) {
            //     // Подставляем значения в соответствующие элементы
            //     packageTime.textContent = selectedPackageTimeIdInput.textContent;
            // }

            // if (selectedPackageWorkingIdInput) {
            //     // Подставляем значения в соответствующие элементы
            //     packageWork.textContent = selectedPackageWorkingIdInput.textContent;
            // }

            // if (selectedPackageDiplomIdInput) {
            //     // Подставляем значения в соответствующие элементы
            //     packageDiplom.textContent = selectedPackageDiplomIdInput.textContent;
            // }
        }
    });
});

packageInputs.forEach(function(input) {
    input.addEventListener('change', function() {
        // Находим выбранный пакет
        const selectedPackage = Array.from(packageNames).find(packageName => packageName.textContent === this.parentNode.querySelector('h1').textContent);

        // Проверяем, найден ли пакет
        if (selectedPackage) {
            // Подставляем значение в атрибут id у элемента с идентификатором "packageTitle"
            packageTitle.textContent = selectedPackage.textContent;
            
            // Получаем значение атрибута data-package-id
            const packageId = this.getAttribute('data-package-id');
            
            // Создаем соответствующие идентификаторы
            const selectedPackageLevelId = `packageLevelInput_${packageId}`;
            const selectedPackageTimeId = `packageTime_${packageId}`;
            const selectedPackageWorkId = `packageWorking_${packageId}`;
            const selectedPackageDiplomId = `packageDiplom_${packageId}`;
            const selectedPackagePriceId = `packagePrice_${packageId}`;

            
            // Находим соответствующие элементы по их уникальным идентификаторам
            const selectedPackageLevelInput = document.getElementById(selectedPackageLevelId);
            const selectedPackageTimeIdInput = document.getElementById(selectedPackageTimeId);
            const selectedPackageWorkingIdInput = document.getElementById(selectedPackageWorkId);
            const selectedPackageDiplomIdInput = document.getElementById(selectedPackageDiplomId);
            selectedPackagePriceIdInput = document.getElementById(selectedPackagePriceId);

            console.log(selectedPackageWorkingIdInput);
            updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput, selectedCheckboxes);

            // Проверяем, найдены ли элементы
            if (selectedPackageLevelInput) {
                // Подставляем значения в соответствующие элементы
                packageSelect.textContent = selectedPackageLevelInput.textContent;
            }

            if (selectedPackageLevelInput) {
                // Подставляем значения в соответствующие элементы
                packageTime.textContent = selectedPackageTimeIdInput.textContent;
            }

            if (selectedPackageWorkingIdInput) {
                // Подставляем значения в соответствующие элементы
                packageWork.textContent = selectedPackageWorkingIdInput.textContent;
            }

            if (selectedPackageDiplomIdInput) {
                // Подставляем значения в соответствующие элементы
                packageDiplom.textContent = selectedPackageDiplomIdInput.textContent;
            }

            
        }
    });
});


function updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput, selectedCheckboxes) {
    // Проверяем, есть ли хотя бы одно из значений
    if (selectedPackagePriceIdInput || selectedCheckboxes.length > 0 || selectedTempPriceIdInput) {
      // Получаем значения из элементов
      const selectedPackagePriceIdInputValue = parseFloat(selectedPackagePriceIdInput.textContent);
      const selectedTempPriceIdInputValue = (selectedTempPriceIdInput.textContent === 'Бесплатно') ? 0 : parseFloat(selectedTempPriceIdInput.textContent);
  
      // Проверяем, является ли selectedTempPriceIdInputValue равным 'Бесплатно'
      if (isNaN(selectedTempPriceIdInputValue)) {
        console.log('Ошибка: Неверное значение для selectedTempPriceIdInput');
        return;
      }
  
      // Вычисляем сумму
      let totalValue = selectedPackagePriceIdInputValue + selectedTempPriceIdInputValue;
  
      // Обрабатываем каждый выбранный чекбокс
      selectedCheckboxes.forEach(function (checkbox) {
        const optionRow = checkbox.parentNode.querySelector('.option__selected');
        const optionPrice = optionRow.querySelector('.option__cost');
        const optionPriceValue = parseFloat(optionPrice.textContent);
        if (!isNaN(optionPriceValue)) {
          totalValue += optionPriceValue;
        }
      });
  
      console.log(totalValue);
  
      // Вставляем сумму в элемент #valueAll
      valueAll.textContent = totalValue.toFixed(2); // Округляем до двух знаков после запятой
    }
  }
  
  
  
  