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
            
            updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput);

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
            updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput);

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


function updateTotalValue(selectedTempPriceIdInput, selectedPackagePriceIdInput) {
    if (selectedPackagePriceIdInput && selectedTempPriceIdInput) {
      // Получаем значения из элементов
      const selectedPackagePriceIdInputValue = parseFloat(selectedPackagePriceIdInput.textContent);
      const selectedTempPriceIdInputValue = (selectedTempPriceIdInput.textContent === 'Бесплатно') ? 0 : parseFloat(selectedTempPriceIdInput.textContent);
  
      // Проверяем, является ли selectedTempPriceIdInputValue равным 'Бесплатно'
      if (isNaN(selectedTempPriceIdInputValue)) {
        console.log('Ошибка: Неверное значение для selectedTempPriceIdInput');
        return;
      }
  
      // Вычисляем сумму
      const totalValue = selectedPackagePriceIdInputValue + selectedTempPriceIdInputValue;
      console.log(totalValue)
  
      // Вставляем сумму в элемент #valueAll
      valueAll.textContent = totalValue.toFixed(2); // Округляем до двух знаков после запятой
    }
  }
